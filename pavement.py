import os
import zipfile

from paver.easy import *


options(
    plugin = Bunch(
        name = 'IPyConsole',
        ext_libs = path('IPyConsole/ext-libs'),
        ext_src = path('IPyConsole/ext-src'),
        source_dir = path('IPyConsole'),
        package_dir = path('..'),
        tests = [],
        excludes = [
            '.DS_Store',  # on Mac
            '.git',
            'ext-src',
            'coverage*',
            'nose*',
            '*.pyc',
        ],
        # skip certain files inadvertently found by exclude pattern globbing
        skip_exclude = []
    ),
)

@task
@cmdopts([
    ('clean', 'c', 'Clean out dependencies first'),
    ('develop', 'd', 'Do not alter source dependency git checkouts'),
])
def setup(options):
    """Install run-time dependencies"""
    clean = getattr(options, 'clean', False)
    develop = getattr(options, 'develop', False)
    ext_libs = options.plugin.ext_libs
    ext_src = options.plugin.ext_src
    if clean:
        ext_libs.rmtree()
    ext_libs.makedirs()
    runtime, test = read_requirements()
    os.environ['PYTHONPATH']=ext_libs.abspath()
    for req in runtime + test:
        if '#egg' in req:
            urlspec, req = req.split('#egg=')
            localpath = ext_src / req
            if not develop:
                if localpath.exists():
                    cwd = os.getcwd()
                    os.chdir(localpath)
                    print(localpath)
                    sh('git pull')
                    os.chdir(cwd)
                else:
                    sh('git clone  %s %s' % (urlspec, localpath))
            req = localpath

        sh('easy_install -a -d %(ext_libs)s %(dep)s' % {
            'ext_libs' : ext_libs.abspath(),
            'dep' : req
        })


def read_requirements():
    """Return a list of runtime and list of test requirements"""
    lines = path('requirements.txt').lines()
    lines = [ l for l in [ l.strip() for l in lines] if l ]
    divider = '# test requirements'

    try:
        idx = lines.index(divider)
    except ValueError:
        raise BuildFailure(
            'Expected to find "%s" in requirements.txt' % divider)

    not_comments = lambda s,e: [ l for l in lines[s:e] if l[0] != '#']
    return not_comments(0, idx), not_comments(idx+1, None)


@task
def install(options):
    """Install plugin to QGIS plugin directory"""
    plugin_name = options.plugin.name
    src = path(__file__).dirname() / plugin_name
    dst = path('~').expanduser() / '.qgis2' / 'python' / 'plugins' / plugin_name
    src = src.abspath()
    dst = dst.abspath()
    if hasattr(src, 'symlink'):
        src.symlink(dst)
    else:
        dst.rmtree()
        src.copytree(dst)


def _make_zip(zipFile, options):
    excludes = set(options.plugin.excludes)
    skips = options.plugin.skip_exclude

    src_dir = options.plugin.source_dir
    exclude = lambda p: any([path(p).fnmatch(e) for e in excludes])
    def filter_excludes(root, items):
        if not items:
            return []
        # to prevent descending into dirs, modify the list in place
        for item in list(items):  # copy list or iteration values change
            itempath = path(os.path.relpath(root)) / item
            if exclude(item) and item not in skips:
                debug('Excluding %s' % itempath)
                items.remove(item)
        return items

    for root, dirs, files in os.walk(src_dir):
        for f in filter_excludes(root, files):
            relpath = os.path.relpath(root)
            zipFile.write(path(root) / f, path(relpath) / f)
        filter_excludes(root, dirs)


@task
@cmdopts([
    ('tests', 't', 'Package tests with plugin'),
])
def package(options):
    """Create plugin package"""
    package_file = options.plugin.package_dir / ('%s.zip' % options.plugin.name)
    with zipfile.ZipFile(package_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        if not hasattr(options.package, 'tests'):
            options.plugin.excludes.extend(options.plugin.tests)
        _make_zip(zf, options)
    return package_file
