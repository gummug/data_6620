# Impact of Student Engagement on Job Placement & Starting Salary

## Description

The Dean’s Office of the Jon M. Huntsman School of Business, utlizies
Salesforce to collect recruitment, enrollment, and post-graduation data
on students. We seek to understand how a student’s involvement with
extracurricular activities, particularly corporate partner engagements,
impact workforce placement and starting salary. With this data, we aim
to understand the efficacy of corporate partner engagements as it
relates to successful student outcomes (i.e., job secured
post-graduation, industry-standard starting salary, etc.)

## Project Organization

- `/code` Scripts with prefixes (e.g., `01_import-data.py`,
  `02_clean-data.py`) and functions in `/code/src`.
- `/data` Simulated and real data, the latter not pushed.
- `/figures` PNG images and plots.
- `/output` Output from model runs, not pushed.
- `/presentations` Presentation slides.
- `/private` A catch-all folder for miscellaneous files, not pushed.
- `/writing` Reports, posts, and case studies.
- `/.venv` Hidden project library, not pushed.
- `.gitignore` Hidden Git instructions file.
- `.python-version` Hidden Python version for the reproducible
  environment.
- `requirements.txt` Information on the reproducible environment.

## Reproducible Environment

After cloning this repository, go to the project’s terminal in Positron
and run `python -m venv .venv` to create the `/.venv` project library,
followed by `pip install -r requirements.txt` to install the specified
library versions.

Whenever you install new libraries or decide to update the versions of
libraries you use, run `pip freeze > requirements.txt` to update
`requirements.txt`.

For more details on using GitHub, Quarto, etc. see [ASC
Training](https://github.com/marcdotson/asc-training).
