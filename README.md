# cleaning-scripts
This is a repository of Python scripts used in the FHIR integration pipeline to clean input data for different external sources.

There are 3 types of scripts:
- `scripts/custom` User defined scripts to address specific task like cleaning a Patient phone number for example
- `scripts/utils` Basic scripts (like capitalize, test if empty, etc.)
- `scripts/logic` Scripts that operate like logic statement and take other scripts as argument

`scripts/custom` can be extended by users, either by completing new scripts or by adding new ones when no one is addressing their needs.



