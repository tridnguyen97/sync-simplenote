from subprocess import check_call
import os

def build_ui():
    try:
        from pyqt_distutils.build_ui import build_ui
        has_build_ui = True
    except ImportError:
        has_build_ui = False
        print("Try to run `poetry add pyqt_distutils`")
    if has_build_ui:
        """Build UI, resources and translations."""

        # build translations
        check_call(['pylupdate6', 'app.pro'])

        lrelease = os.environ.get('LRELEASE_BIN')
        if not lrelease:
            lrelease = 'lrelease'

        check_call([lrelease, 'app.pro'])

        # build UI & resources
        build_ui.run()

def main():
    build_ui()

if __name__ == '__main__':
    main()