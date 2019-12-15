.PHONY: all
all: DS1000DE_Command_QuickReference.txt

DS1000DE_Command_QuickReference.txt: DS1000DE_ProgrammingGuide_EN.pdf
	pdftotext -layout -f 133 -l 135 ${^} ${@}

.PHONY: clean
clean:
	rm -rf *.txt
