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

## Data Story

**Data Context**: The Dean’s Office includes the External Relations
Team, which works with alumni and corporate partners to coordinate
engagements and develop hiring pipelines. The External Relations Team
aims to create opportunities for students to connect with industry
professionals, with the intent to enhance students’ chances for job
placement and higher starting salaries.

**Data Question**: The External Relations Team wants to understand
whether attending alumni and corporate partner engagements correlates
with better job placement and higher starting salaries for students. To
answer this question, a causal inference analysis will be leveraged to
identify if there’s a cause-and-effect relationship between engagement
events and post-graduation outcomes.

**Data Sources**: The Dean’s Office collects event attendance data
inconsistently and uses a non-required survey to gather job placement
and salary data from students after graduation. Since not all students
respond to the survey, LinkedIn is used to verify if a student has found
a job after graduation and if so, Glassdoor is used to estimate their
starting salary based on experience, job title, and job location.

**Data Challenges**: The External Relations Team faces several data
challenges in determining whether alumni and corporate partner
engagements truly influence student outcomes. Attendance at engagement
events isn’t always tracked consistently, which leaves gaps in
understanding how often and how deeply students participate. The
optional graduation survey can skew results due to response bias, and,
for non-respondents, the use of LinkedIn and Glassdoor introduces
uncertainty—LinkedIn profiles may not be current, and Glassdoor salary
estimates aren’t always precise. Finally, establishing causation rather
than simple correlation requires collecting and controlling for factors
like GPA or prior internships, ensuring that any observed effect on job
placement or starting salary actually stems from engagement rather than
preexisting differences among students.

**Data Solutions**: One approach might be to standardize how attendance
is recorded, requiring sign-ins or using digital registration tools to
fill gaps and create a more accurate measure of student participation.
Offering small incentives for the graduation survey or making it a
graduation checkpoint could improve response rates and reduce bias. For
students who do not respond, the External Relations Team might consider
documenting a confidence level for any inferred salary data from
LinkedIn or Glassdoor, clarifying that these numbers are estimates. To
address the challenge of proving causation, collecting additional
information—such as GPA, internship history, and relevant
extracurricular activities—would allow for stronger statistical methods,
like propensity score matching or regression analyses, that control for
preexisting differences among students.

**Data Impact**: If the analysis shows that engagement events positively
influence students’ job prospects and salaries, the External Relations
Team may decide to prioritize these activities more and develop
student-facing messaging highlighting the positive impacts of
participation. However, if no meaningful relationship is found, the
External Relations Team may adjust overall strategy and shift focus to
other efforts that have a more significant impact on student outcomes.

**Data Presentation**: To ensure the findings are both accessible and
actionable, an interactive dashboard could be developed that showcases
key metrics, such as event attendance trends, job placement rates, and
salary distributions. Simplifying complex analyses—like propensity score
matching—into clear visuals or brief summaries would help non-technical
stakeholders understand how engagement impacts student outcomes. Sharing
statistical findings in student-facing messaging could further
underscore the real-world benefits of attending events, while concise
executive summaries would enable leadership to quickly grasp the main
conclusions and decide on resource allocation.

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
