# Retrieval Protocol

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Retrieval protocol specification  
**Date:** 2026-01-25  
**Phase:** 6  
**Status:** Definitive specification

---

## PURPOSE

This document establishes the mandatory retrieval protocol for the Course Assistant AI agent. All agent responses involving course facts, assignment requirements, pacing, and planning must follow these step-by-step rules to ensure accurate, consistent, and deterministic retrieval behavior with proper source citation.

---

## CORE RETRIEVAL PRINCIPLES

### 1. INDEX-First Retrieval
**Rule:** Always consult the INDEX first to locate content before attempting direct file access.

**Rationale:** The INDEX provides the authoritative map of what content exists, where it is located, and what entity IDs and section anchors to use for precise retrieval.

### 2. Smallest Retrievable Unit
**Rule:** Retrieve content at the section level using anchor IDs, not whole documents.

**Rationale:** Section-level retrieval minimizes token usage, improves accuracy, and enables precise citation.

### 3. Authority Hierarchy Enforcement
**Rule:** Always respect the 6-tier authority hierarchy defined in `04_Authority_and_Precedence_Rules.md`.

**Hierarchy (Quick Reference):**
1. **Course Schedule** → Dates, times, deadlines
2. **Course Core** → Policies, grading, structure
3. **Student Profile** → Student context, preferences
4. **INDEX** → File/section locations
5. **Module Manifests** → Module content inventory
6. **Module Working Memory Files** → Detailed execution support

### 4. Mandatory Citation
**Rule:** Every response that references course information MUST include a source citation using the format: `filename#section-anchor (entity_id)`

### 5. No Synthesis for Requirements
**Rule:** Do NOT synthesize, infer, or guess course requirements. Extract only what is explicitly stated in authoritative sources.

**When information is missing:** State `"Not found in provided materials"` and suggest where to find it.

### 6. Conflict Flagging
**Rule:** When contradictions are detected between sources, explicitly flag the conflict, report both sources, and defer to the higher-authority source per the hierarchy.

---

## RETRIEVAL PROTOCOL BY QUERY TYPE

### PROTOCOL A: Course Fact Queries
**Query Examples:**
- "What is the late work policy?"
- "How much is the midterm worth?"
- "What are the attendance requirements?"

**Step-by-Step Process:**

**Step 1:** Identify query type as policy, grading, or structural requirement.

**Step 2:** Consult INDEX to locate the authoritative section.
- For policies → `course_core.md#[policy-section-id]`
- For grading → `course_core.md#grading-policy`
- For structure → `course_core.md#[structure-section-id]`

**Step 3:** Retrieve content from the identified section using the anchor ID.

**Step 4:** Extract the specific fact requested. Do NOT paraphrase or summarize unless the exact text is too long.

**Step 5:** Cite the source using the format: `Source: course_core.md#section-anchor`

**Example Response:**

```
Late work policy: Accepted up to 48 hours after deadline with 10% penalty per day.

Source: course_core.md#late-work-policy
```

**Failure Behavior:**
If the information is not found in `course_core.md`:
```
Not found in provided materials.

The late work policy is not specified in course_core.md.

Suggestions:
- Check the original syllabus
- Ask the instructor for clarification
```

---

### PROTOCOL B: Date and Deadline Queries
**Query Examples:**
- "When is Assignment A03 due?"
- "What are the dates for Module 5?"
- "When is the final exam?"

**Step-by-Step Process:**

**Step 1:** Identify the entity type (assignment, exam, module, reading, discussion, milestone).

**Step 2:** Consult INDEX to locate the entity.
- Search `entities.assignments` for assignment IDs
- Search `entities.exams` for exam IDs
- Search `entities.modules` for module IDs
- Etc.

**Step 3:** Extract `due_date_display`, `due_date_iso`, and `due_time` (if applicable) from the entity record.

**Step 4:** Extract `authoritative_section` reference.

**Step 5:** Retrieve the authoritative section from `course_schedule.md` to confirm the date.

**Step 6:** Respond with both display date and time, including timezone.

**Step 7:** Cite the source using the format: `Source: course_schedule.md#section-anchor (entity_id)`

**Example Response:**

```
Assignment A03 is due Monday, Feb 10, 2026 at 11:59 PM CT.

Source: course_schedule.md#assignment-calendar (A03)
```

**Conflict Handling:**
If a module file states a different date than `course_schedule.md`:

```
CONFLICT DETECTED:

course_schedule.md#assignment-calendar (A03) states: Due Monday, Feb 10, 2026 at 11:59 PM
M03/Assignment_A03_Instructions.pdf states: Due February 12, 2026

The Grounded Knowledge File (course_schedule.md) is the authoritative source for dates.

Assignment A03 is due: Monday, Feb 10, 2026 at 11:59 PM CT

Source: course_schedule.md#assignment-calendar (A03) [AUTHORITATIVE]

Note: The module instruction file lists a different date (February 12). If this is a course update, please update course_schedule.md and regenerate the INDEX.
```

**Failure Behavior:**
If the due date is listed as `TBD`:

```
Assignment A07 due date: TBD (To Be Determined)

Source: course_schedule.md#assignment-calendar (A07)

This due date has not been announced yet. Please check Canvas for updates or ask the instructor.
```

---

### PROTOCOL C: Assignment Requirement Queries
**Query Examples:**
- "What are the requirements for Assignment A03?"
- "How long should Assignment A05 be?"
- "What format should I use for the final project?"

**Step-by-Step Process:**

**Step 1:** Consult INDEX to locate the assignment entity.
- Search `entities.assignments` for the assignment ID

**Step 2:** Extract `authoritative_section` (in `course_schedule.md`) and `related_sections` (which may include module files).

**Step 3:** Retrieve high-level information from `course_schedule.md#assignment-calendar`.
- Assignment title
- Due date
- Module association
- Brief description (if available)

**Step 4:** Check `related_sections` for detailed instruction files in module packages.
- Example: `M03/Assignment_A03_Instructions.pdf`

**Step 5:** Retrieve detailed requirements from the module instruction file.

**Step 6:** Synthesize response:
- State due date and basic info from `course_schedule.md` (AUTHORITATIVE)
- Provide detailed requirements from module files (SUPPORTIVE)
- Cite BOTH sources

**Step 7:** If a rubric file exists, reference it.

**Example Response:**

```
Assignment A03: Marketing Strategy Analysis

**Due Date:** Monday, Feb 10, 2026 at 11:59 PM CT
**Source:** course_schedule.md#assignment-calendar (A03)

**Requirements (from detailed instructions):**
- Length: 5-7 pages, double-spaced
- Format: APA style with title page and references
- Required sections:
  1. Industry analysis using Porter's Five Forces
  2. Competitive positioning analysis
  3. Strategic recommendations (minimum 3)
- Submission: Upload PDF to Canvas

**Rubric:**
- Industry analysis (40 points)
- Competitive positioning (30 points)
- Strategic recommendations (20 points)
- Writing quality and APA formatting (10 points)

**Sources:**
- course_schedule.md#assignment-calendar (A03) [dates and basic info]
- M03/Assignment_A03_Instructions.pdf [detailed requirements]
- M03/Assignment_A03_Rubric.pdf [grading criteria]

Would you like help with any specific section of this assignment?
```

**Failure Behavior:**
If detailed requirements are not found in module files:

```
Assignment A05: Final Reflection Essay

**Due Date:** Monday, Apr 14, 2026 at 11:59 PM CT
**Source:** course_schedule.md#assignment-calendar (A05)

**Requirements:** Not found in provided materials.

The detailed requirements for Assignment A05 are not specified in course_schedule.md, and no instruction file was found in the uploaded module materials.

Suggestions:
- Check if Module 5 has been uploaded
- Consult the original assignment instructions from Canvas
- Ask the instructor for clarification

Would you like me to check uploaded module files for this information?
```

---

### PROTOCOL D: Pacing and Planning Queries
**Query Examples:**
- "What should I work on this week?"
- "What assignments are coming up?"
- "Am I on track?"
- "What is overdue?"

**Step-by-Step Process:**

**Step 1:** Determine the current date (use today's date as reference).

**Step 2:** Consult INDEX to retrieve all date-based entities:
- `entities.assignments`
- `entities.exams`
- `entities.discussions`
- `entities.milestones`

**Step 3:** Filter entities by date ranges:
- **Overdue:** `due_date_iso < current_date`
- **This week:** `current_date <= due_date_iso <= current_date + 7 days`
- **Next week:** `current_date + 7 < due_date_iso <= current_date + 14 days`
- **Upcoming (2-4 weeks):** `current_date + 14 < due_date_iso <= current_date + 28 days`

**Step 4:** Consult `student_profile.md#progress-tracking` to identify completed modules or assignments.

**Step 5:** Generate pacing recommendations based on:
- Upcoming deadlines
- Student availability (from `student_profile.md#constraints`)
- Time estimates (from module manifests or assignment details)

**Step 6:** Present results in order: Overdue → This Week → Next Week → Upcoming.

**Step 7:** Cite sources for all dates and deadlines.

**Required Assumptions Disclosure:**
When generating pacing recommendations, explicitly state assumptions:
- "Assuming you have not yet started Assignment A03..."
- "Based on the module estimate of 8-10 hours..."
- "If you work 2 hours per day..."

**Example Response:**

```
**Pacing Check (as of Monday, Feb 03, 2026)**

**OVERDUE:**
None

**THIS WEEK (Feb 03 - Feb 09):**

1. **Discussion D03** - Due Friday, Feb 07, 2026 at 11:59 PM CT
   - Source: course_schedule.md#discussion-schedule (D03)
   - Estimated time: 1-2 hours

2. **Assignment A03: Marketing Strategy Analysis** - Due Monday, Feb 10, 2026 at 11:59 PM CT
   - Source: course_schedule.md#assignment-calendar (A03)
   - Estimated time: 8-10 hours
   - Status: Due at end of week/early next week
   - Recommendation: Start this week to avoid last-minute rush

**NEXT WEEK (Feb 10 - Feb 16):**

3. **Quiz Q02** - Due Wednesday, Feb 12, 2026 at 11:59 PM CT
   - Source: course_schedule.md#assignment-calendar (Q02)
   - Estimated time: 30 minutes

4. **Group Project Milestone MS01** - Due Friday, Feb 14, 2026 at 5:00 PM CT
   - Source: course_schedule.md#milestone-timeline (MS01)
   - Your role: Data analysis lead
   - Source: student_profile.md#group-project-context

**UPCOMING (2-4 weeks):**

5. **Midterm Exam** - Wednesday, Mar 05, 2026 at 2:00 PM CT
   - Source: course_schedule.md#exam-schedule (MIDTERM)

**Pacing Recommendation:**

This week (Module 3):
- Complete Discussion D03 by Friday (1-2 hours)
- Start Assignment A03 early in the week (8-10 hours total)
- Review Module 3 lecture slides and readings (3-4 hours)

Assumptions:
- You have not yet started Assignment A03
- You plan to work 10-12 hours on coursework this week
- Based on your student profile, you have Sunday-Tuesday evenings available

Source: student_profile.md#constraints, student_profile.md#study-approach

Would you like a detailed breakdown for Assignment A03?
```

**Failure Behavior:**
If `student_profile.md#progress-tracking` is not maintained:

```
I cannot determine what you have completed because progress tracking is not maintained in student_profile.md.

To enable accurate pacing recommendations:
1. Update student_profile.md#progress-tracking with completed modules and assignments
2. Regenerate the INDEX
3. Re-upload both files

For now, I can show you all upcoming deadlines. Would you like to see that instead?
```

---

### PROTOCOL E: Module Content Queries
**Query Examples:**
- "What is in Module 3?"
- "Show me the readings for Module 5"
- "What are the learning objectives for Module 2?"

**Step-by-Step Process:**

**Step 1:** Consult INDEX to locate the module entity.
- Search `entities.modules` for the module ID

**Step 2:** Extract module metadata:
- `start_date_display`, `start_date_iso`
- `end_date_display`, `end_date_iso`
- `module_folder`
- `manifest_file`

**Step 3:** Retrieve module overview from the module manifest:
- `{module_id}.module_manifest.md#overview`

**Step 4:** Retrieve file inventory from the module manifest:
- `{module_id}.module_manifest.md#file-inventory`

**Step 5:** Cross-reference with INDEX to find assignments, readings, discussions associated with this module.

**Step 6:** Present module summary with:
- Module title and dates (from `course_schedule.md`)
- Learning objectives (from module manifest)
- File inventory (from module manifest)
- Associated assignments/readings/discussions (from INDEX)

**Step 7:** Cite all sources.

**Example Response:**

```
Module 3: Competitive Strategy (M03)

**Dates:** Monday, Feb 03, 2026 to Sunday, Feb 09, 2026
Source: course_schedule.md#module-sequence (M03)

**Learning Objectives:**
- Analyze industry structure using Porter's Five Forces
- Identify sources of competitive advantage
- Evaluate strategic positioning options
- Apply competitive analysis to real-world cases

Source: M03/M03.module_manifest.md#overview

**Module Materials:**
- Lecture slides: Module_03_Lecture_Slides.pptx (45 slides)
- Lecture video: Module_03_Lecture_Video.mp4 (90 minutes)
- Reading: Reading_Porter_Ch1.pdf
- Assignment instructions: Assignment_A03_Instructions.pdf
- Assignment rubric: Assignment_A03_Rubric.pdf
- Discussion prompt: Discussion_D03_Prompt.md
- Case study: Case_Study_Tesla.pdf

Source: M03/M03.module_manifest.md#file-inventory

**Assignments Due in Module 3:**
- Assignment A03: Due Monday, Feb 10, 2026 at 11:59 PM CT

**Discussions:**
- Discussion D03: Opens Monday, Feb 03, 2026 | Closes Friday, Feb 07, 2026

Sources: course_schedule.md#assignment-calendar, course_schedule.md#discussion-schedule

**Estimated Time Commitment:** 8-10 hours
Source: M03/M03.module_manifest.md#overview

Would you like more details about any specific material?
```

**Failure Behavior:**
If module has not been uploaded:

```
Module 5: [Module title from course_schedule.md]

**Dates:** [dates from course_schedule.md]
Source: course_schedule.md#module-sequence (M05)

**Module materials:** Not yet uploaded.

The Module 5 package has not been uploaded. To access detailed module content, learning objectives, and files:
1. Upload the M05/ folder or M05.zip
2. Verify the module using the verification prompt
3. Update the INDEX

I can show you what assignments and readings are scheduled for Module 5 based on the course schedule. Would you like to see that?
```

---

## CITATION STANDARDS

### Citation Format Requirements

**For course facts (policies, grading, structure):**
```
[Answer]

Source: course_core.md#section-anchor
```

**For dates and deadlines:**
```
[Answer]

Source: course_schedule.md#section-anchor (entity_id)
```

**For student context:**
```
[Answer]

Source: student_profile.md#section-anchor
```

**For module content (Working Memory Files):**
```
[Answer]

Source: module_id/filename (uploaded module content)
```

**For multi-source answers:**
```
[Answer]

Sources:
- course_schedule.md#section-anchor (entity_id) [authoritative for dates]
- module_id/filename [detailed requirements]
```

### Required Citation Elements

1. **Filename** (exact match, including extension)
2. **Section anchor** (format: `#section-name`)
3. **Entity ID** (when applicable, in parentheses)
4. **Authority indicator** (when citing multiple sources, mark which is authoritative)

---

## CONFLICT RESOLUTION IN RETRIEVAL

### Conflict Type 1: Date/Time Contradiction

**Detection:** Same entity has different dates in different sources.

**Resolution Protocol:**
1. Flag the conflict explicitly using "CONFLICT DETECTED:"
2. Report both sources and their values
3. Defer to `course_schedule.md` (Tier 1 authority for dates)
4. State which source is authoritative
5. Suggest user action if needed

**Example:**
```
CONFLICT DETECTED:

course_schedule.md#assignment-calendar (A03) states: Due Monday, Feb 10, 2026 at 11:59 PM
M03/Assignment_A03_Instructions.pdf states: Due February 12, 2026

The Grounded Knowledge File (course_schedule.md) is the authoritative source for dates.

Assignment A03 is due: Monday, Feb 10, 2026 at 11:59 PM CT

Source: course_schedule.md#assignment-calendar (A03) [AUTHORITATIVE]

Note: The module instruction file lists a different date (February 12). If this is a course update, please update course_schedule.md and regenerate the INDEX.
```

### Conflict Type 2: Policy Contradiction

**Detection:** Same policy stated differently in different sources.

**Resolution Protocol:**
1. Flag the conflict
2. Defer to `course_core.md` (Tier 2 authority for policies)
3. Cite authoritative source
4. Note the contradiction

**Example:**
```
CONFLICT DETECTED:

course_core.md#late-work-policy states: Late work accepted up to 48 hours with 10% penalty per day
M02/Assignment_Instructions.pdf states: No late work accepted

The course_core.md late work policy is the authoritative source unless there has been a course update.

Late work policy: Accepted up to 48 hours after deadline with 10% penalty per day.

Source: course_core.md#late-work-policy [AUTHORITATIVE]

Note: Module 2 assignment document states no late work accepted. The course core policy is the default unless this specific assignment has a different policy. Please confirm with the instructor if needed.
```

### Conflict Type 3: Missing Information

**Detection:** Information requested but not found in any Grounded Knowledge File.

**Resolution Protocol:**
1. State: `"Not found in provided materials"`
2. Do NOT invent, infer, or guess
3. Suggest where to find the information
4. Offer to check module files if applicable

**Example:**
```
Not found in provided materials.

The page length requirement for Assignment A05 is not specified in course_core.md or course_schedule.md.

Suggestions:
- Check the Module 5 assignment document if you've uploaded it
- Consult the original assignment instructions from Canvas
- Email the instructor for clarification

Would you like me to check uploaded module files for this information?
```

---

## SPECIAL RETRIEVAL SCENARIOS

### Scenario 1: Retrieve Assignment Rubric

**Query:** "What is the rubric for Assignment A03?"

**Process:**
1. Locate assignment entity in INDEX
2. Check `related_sections` for rubric file
3. If rubric file exists in module package → Reference it
4. If rubric is embedded in `course_core.md#grading-policy` → Extract it
5. If not found → State "Not found in provided materials"

**Example Response:**
```
The grading rubric for Assignment A03 is available in:

M03/Assignment_A03_Rubric.pdf

This file is in the uploaded Module 3 package. The rubric includes:
- Industry analysis (40 points)
- Competitive positioning (30 points)
- Strategic recommendations (20 points)
- Writing quality and APA formatting (10 points)

Source: M03/Assignment_A03_Rubric.pdf (uploaded module content)

Would you like me to explain any specific rubric criteria?
```

### Scenario 2: Retrieve Group Project Context

**Query:** "What is my role in the group project?"

**Process:**
1. Consult `student_profile.md#group-project-context`
2. Extract student role, responsibilities, and team structure
3. Cross-reference with `course_schedule.md#milestone-timeline` for upcoming milestones
4. Identify which milestones the student is responsible for

**Example Response:**
```
Your role in the Final Group Project (GP01):

**Your Role:** Data Analysis Lead
**Your Responsibilities:**
- Collect and analyze quantitative data for the project
- Create data visualizations and charts
- Present findings to the team
- Contribute to the final report's data analysis section

**Team Structure:**
- Project Manager: Member 01
- Research Lead: Member 02
- Data Analysis Lead: You (Josh)
- Presentation Lead: Member 03

Source: student_profile.md#group-project-context

**Upcoming Milestones You Own:**
- MS01: Team Formation & Role Assignment - Due Friday, Feb 14, 2026 at 5:00 PM CT
  (All team members participate)
- MS02: Data Collection Complete - Due Friday, Mar 07, 2026 at 5:00 PM CT
  (Your primary responsibility)

Source: course_schedule.md#milestone-timeline

Would you like help planning for the data collection milestone?
```

### Scenario 3: Check Progress and Completion Status

**Query:** "What have I completed so far?"

**Process:**
1. Consult `student_profile.md#progress-tracking`
2. List completed modules and assignments
3. Compare against `course_schedule.md` to identify what remains
4. If progress tracking is not maintained → State limitation

**Example Response (if maintained):**
```
Based on your progress tracking:

**Completed Modules:**
- Module 1 ✓
- Module 2 ✓

**Completed Assignments:**
- Assignment A01 ✓ (Submitted Jan 20, 2026)
- Assignment A02 ✓ (Submitted Jan 27, 2026)
- Quiz Q01 ✓ (Completed Jan 24, 2026)
- Discussion D01 ✓
- Discussion D02 ✓

**Current Focus:**
- Module 3 (in progress)

Source: student_profile.md#progress-tracking

**Remaining Work:**
- Modules 3-12 (10 modules)
- Assignments A03-A10 (8 assignments)
- Quizzes Q02-Q05 (4 quizzes)
- Discussions D03-D12 (10 discussions)
- Midterm Exam
- Final Exam
- Group Project (3 milestones)

Source: course_schedule.md (cross-referenced with progress tracking)

You are currently on track for Module 3 (week 3 of 15).

Would you like a detailed breakdown of upcoming work?
```

**Example Response (if not maintained):**
```
Progress tracking is not currently maintained in student_profile.md.

To track your progress:
1. Update student_profile.md#progress-tracking with:
   - Completed modules
   - Completed assignments (with submission dates)
   - Current focus area
2. Regenerate the INDEX
3. Re-upload both files

Once updated, I can provide detailed progress reports and personalized pacing recommendations.

Would you like help updating your progress tracking section?
```

---

## AGENT VERIFICATION CHECKLIST

Before every response involving course information, the agent must verify:

1. ☐ **Is this a date or deadline?**  
   → Consult `course_schedule.md` FIRST (Tier 1)

2. ☐ **Is this a policy, rule, or grading component?**  
   → Consult `course_core.md` FIRST (Tier 2)

3. ☐ **Is this student-specific context?**  
   → Consult `student_profile.md` FIRST (Tier 3)

4. ☐ **Do I need to locate a specific section or entity?**  
   → Consult `INDEX.json` FIRST (Tier 4)

5. ☐ **Is this detailed assignment content?**  
   → Check INDEX for module references, then consult module manifest (Tier 5), then module files (Tier 6)

6. ☐ **Are there conflicting sources?**  
   → Apply conflict resolution rules (Protocols above)

7. ☐ **Is information missing?**  
   → State "Not found in provided materials"

8. ☐ **Have I cited my sources correctly?**  
   → Include `filename#section-anchor` and `entity_id`

---

## TOKEN AND CHUNKING CONSTRAINTS

### Maximum Retrieval Size
- **Per section:** Retrieve only the specific section requested, not the entire file
- **Use anchors:** Always use section anchors to limit scope
- **Character limits:** If a section exceeds 2000 characters, summarize key points and offer to provide subsections

### Chunking Strategy
When a response requires large amounts of content:
1. Provide a summary first
2. Offer to break down into smaller parts
3. Ask which subsection the user wants details on

**Example:**
```
Assignment A03 has detailed requirements across multiple areas. Here's a summary:

1. Length & Format: 5-7 pages, APA style
2. Required Sections: Industry analysis, Competitive positioning, Recommendations
3. Grading: 100 points across 4 criteria

Which area would you like me to detail first?
```

---

## FAILURE BEHAVIORS

### When Grounded Knowledge Files Contradict Each Other

**This should NOT happen** if files are properly maintained. If detected:

1. Flag as **SYSTEM ERROR**
2. Report contradiction to user
3. Ask user to verify and correct
4. Do NOT proceed with answer until resolved

**Example:**
```
SYSTEM ERROR DETECTED:

course_core.md#grading-policy states: Participation is 15% of grade
course_schedule.md#metadata (source_files) references a syllabus stating: Participation is 20% of grade

This is a contradiction within Grounded Knowledge Files. Please verify which is correct and update the incorrect file.

I cannot provide a reliable answer until this is resolved.
```

### When INDEX is Stale (References Missing Files)

**This should NOT happen** if INDEX is regenerated after updates. If detected:

1. Flag as **INDEX STALE warning**
2. Attempt to answer using direct file search
3. Remind user to regenerate INDEX

**Example:**
```
INDEX STALE WARNING:

INDEX.json references section course_schedule.md#milestone-timeline, but this section was not found in the current file.

I will search course_schedule.md directly for milestone information.

Reminder: Please regenerate the INDEX after any Grounded Knowledge File update.

[Answer based on direct search]
```

### When User Asks for Information Outside Scope

**Example:** User asks about a different course or term.

**Response:**
```
I am configured for MGMT-5001-SEC01-2025-FA (Management 5001, Section 01, Fall 2025) only.

The question you asked appears to be about a different course or term. I cannot answer questions outside this course scope.

If you need assistance with another course, please use a separate Course Assistant agent configured for that course.
```

---

## SUMMARY: RETRIEVAL PROTOCOL HIERARCHY

**Step 1: Classify Query Type**
- Course fact → Protocol A
- Date/deadline → Protocol B
- Assignment requirement → Protocol C
- Pacing/planning → Protocol D
- Module content → Protocol E

**Step 2: Consult INDEX First**
- Locate entity or section
- Identify authoritative source
- Check for related sections

**Step 3: Retrieve from Authoritative Source**
- Use section anchors
- Extract smallest unit needed
- Respect authority hierarchy

**Step 4: Check for Conflicts**
- Compare sources if multiple exist
- Flag contradictions
- Defer to higher-authority source

**Step 5: Cite Sources**
- Use required citation format
- Include filename, anchor, entity ID
- Mark authoritative source when multiple cited

**Step 6: Handle Missing Data**
- State "Not found in provided materials"
- Suggest where to find info
- Do NOT guess or infer

---

## ENFORCEMENT

This retrieval protocol is **MANDATORY** for all agent responses involving course information. No exceptions.

Violations constitute a system failure and must be corrected immediately.

---

**END OF DOCUMENT**