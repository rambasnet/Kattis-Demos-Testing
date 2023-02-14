# provide path to where plantuml.jar is downloaded
PLANTUML = java -jar ~/plantuml.jar
DOCS = docs

all: check_types unittest localtest create_docs create_uml
	@echo "All done!"

unittest:
ifeq ($(shell which pytest), ) # if pytest not found
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest test_hello.py
	pytest test_main.py
	@echo "All unittesting worked!"

localtest:
	@python main.py | diff - data/1.ans
	@echo "Program worked on sample data!" 

check_types:
# use shell command which to check if mypy is installed and is in $PATH
ifeq ($(shell which mypy), )
	@echo "mypy not found. Installing mypy..."
	pip install mypy
endif
	mypy --disallow-untyped-defs --strict main.py hello.py
	#mypy --disallow-untyped-defs --strict hello.py
	mypy --disallow-untyped-defs --strict test_hello.py
	mypy --disallow-untyped-defs --strict test_main.py
	@echo "Type checking done."

create_doc_folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

create_docs: create_doc_folder
	pdoc --force -o docs main.py hello.py # creates .md docs inside docs
	pdoc --force --html -o docs main.py hello.py # creates html docs inside docs
	@echo "html docs created and saved in $(DOCS)"

create_uml: create_doc_folder
# use shell command which to check if java is installed and is in the $PATH
ifeq ($(shell which java), )
	$(error "No java found in $(PATH). Install java to run plantuml")
endif
# use wildcard function to check if file exists
ifeq ($(wildcard ~/plantuml.jar), )
	@echo "Downloading plantuml.jar in home folder..."
	curl -L -o ~/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
endif
	$(PLANTUML) uml/HelloWorld.plantuml
	$(PLANTUML) uml/Main.plantuml
	$(PLANTUML) uml/solution.plantuml
	@echo "UML diagrams created and saved in uml folder"

