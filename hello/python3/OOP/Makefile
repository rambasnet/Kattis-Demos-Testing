
# provide path to where plantuml.jar is downloaded
PLANTUML = java -jar ~/plantuml.jar
DOCS = docs 

all: check_types unittest localtest create_docs create_uml
	@echo "All done!"

unittest:
	pytest test_hello.py
	pytest test_main.py
	@echo "All unittesting worked!"

localtest:
	@python main.py | diff - data/1.ans
	@echo "Program worked on sample data!" 

check_types:
	mypy --disallow-untyped-defs --strict main.py hello.py
	#mypy --disallow-untyped-defs --strict hello.py
	mypy --disallow-untyped-defs --strict test_hello.py
	mypy --disallow-untyped-defs --strict test_main.py
	@echo "Type checking done."

create_doc_folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

create_docs: create_doc_folder
	pdoc --force -o docs main.py hello.py # creates .md docs in docs
	pdoc --force --html -o docs main.py hello.py # creates html docs in docs
	@echo "html docs created and saved in $(DOCS)"

create_uml: create_doc_folder
	$(PLANTUML) uml/HelloWorld.plantuml
	$(PLANTUML) uml/Main.plantuml
	$(PLANTUML) uml/solution.plantuml
	@echo "UML diagrams created and saved in $(DOCS)"
