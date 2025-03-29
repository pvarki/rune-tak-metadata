all: sync

sync: sync-en sync-fi

sync-en: ServiceTak.en.json ../../../../../assets/locale/en.json
	./merge-translations.py -t ServiceTak.en.json -s ../../../../../assets/locale/en.json -o ServiceTak.en.json

sync-fi: ServiceTak.fi.json ../../../../../assets/locale/fi.json
	./merge-translations.py -t ServiceTak.fi.json -s ../../../../../assets/locale/fi.json -o ServiceTak.fi.json
