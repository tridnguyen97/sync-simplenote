# sync-simplenote
Sync recently modified notes in Simplenote to Notion.

## Installation
After cloning the project, running following command:
```
poetry install
```

## Getting started

In development environment, to build resources, UI and translations:
```
poetry run prepare
```
Then starting the project:
```
poetry run dev
```

## Building executable file
```
poetry run build
```

## Miscellaneous
To create or modify qt designer files, pyside6 designer tool can be used:
```
poetry run pyside6-designer <filename>.ui
```