from subprocess import check_call
import os
from subprocess import CalledProcessError

SUPPORTED_LANGUAGE = ['ca_ES', 'en_US', 'es_ES', 'fr_FR']
TRANSLATION_DIR = os.path.join(os.getcwd(), 'resources/translations')
UI_DIR = os.path.join(os.getcwd(), 'resources/views')    

def build_ui(langs=SUPPORTED_LANGUAGE):
    """Build UI, resources and translations."""
    for view in os.listdir(UI_DIR):
        view_dir = os.path.join(UI_DIR, view)
        if os.path.isfile(view_dir):
            # build UI, no sub-directories
            view_module = os.path.join(UI_DIR, f'{view.rstrip(".ui")}_ui.py')
            try:
                check_call(['pyside6-uic', view_dir, '-o', view_module])
            except CalledProcessError as e:
                print(e.stdout)
                break
            # build translations
            for lang in langs:
                lang_dir = os.path.join(TRANSLATION_DIR, f'{lang}.ts')
                binary_dir = os.path.join(TRANSLATION_DIR, f'{lang}.qm')
                try: 
                    check_call(['pyside6-lupdate', view_dir, '-ts', lang_dir])
                    check_call(['pyside6-lrelease', lang_dir, '-qm', binary_dir])
                except CalledProcessError as e:
                    print(e.stdout)
                    break

    # build resources
    resource_module = os.path.join(os.getcwd(), 'resources/views/resources_rc.py')
    resource_dir = os.path.join(os.getcwd(), 'resources/resources.qrc')
    check_call(['pyside6-rcc', resource_dir , '-o', resource_module])

def main():
    build_ui()

if __name__ == '__main__':
    main()