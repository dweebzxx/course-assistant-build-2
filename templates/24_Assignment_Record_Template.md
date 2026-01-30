# Assignment Record Template

---

## Metadata
<!-- REQUIRED: Complete all fields before use -->

| Field | Value |
|-------|-------|
| **assignment_id** | {ASSIGNMENT_ID} |
| **course_id** | {COURSE_ID} |
| **term_id** | {TERM_ID} |
| **module_id** | {MODULE_ID or null} |
| **doc_type** | assignment_record |
| **last_updated** | {YYYY-MM-DD} |
| **timezone** | America/Chicago |
| **source_files** | {comma-separated list of original source filenames} |

---

## Assignment Overview
<!-- anchor: #assignment-overview -->

### Identification
<!-- anchor: #identification -->

| Field | Value |
|-------|-------|
| **Assignment ID** | {ASSIGNMENT_ID} |
| **Assignment Title** | {Full assignment title} |
| **Assignment Type** | {Essay / Quiz / Exam / Project / Discussion / Lab / Homework / Other} |
| **Type Code** | {ESSAY / QUIZ / EXAM / PROJ / DISC / LAB / HW / A} |
| **Associated Module** | {MODULE_ID: Module Title} or None |
| **Points Possible** | {N points} |
| **Weight** | {N% of final grade} or {See course_core.md#grading-policy} |

### Schedule
<!-- anchor: #schedule -->

| Field | Value |
|-------|-------|
| **Assigned Date (display)** | {DayOfWeek, Mon DD, YYYY} or TBD |
| **Assigned Date (ISO)** | {YYYY-MM-DD} or null |
| **Due Date (display)** | {DayOfWeek, Mon DD, YYYY} or TBD |
| **Due Date (ISO)** | {YYYY-MM-DD} or null |
| **Due Time** | {h:mm AM/PM} or null |
| **Late Deadline (display)** | {DayOfWeek, Mon DD, YYYY} or N/A |
| **Late Deadline (ISO)** | {YYYY-MM-DD} or null |
| **Late Penalty** | {See course_core.md#late-work-policy} |

### Status
<!-- anchor: #status -->

| Field | Value |
|-------|-------|
| **Current Status** | {Not Started / In Progress / Submitted / Graded} |
| **Submission Date (ISO)** | {YYYY-MM-DD} or null |
| **Grade Received** | {N/N points} or {N%} or Pending |

---

## Assignment Description
<!-- anchor: #assignment-description -->

### Overview
<!-- anchor: #overview -->

{2-3 sentence description of the assignment purpose and what students will do.}

### Learning Objectives Assessed
<!-- anchor: #learning-objectives-assessed -->

This assignment assesses the following learning objectives:

1. {Learning objective 1 - from module or course level}
2. {Learning objective 2}
3. {Learning objective 3}

---

## Requirements
<!-- anchor: #requirements -->

<!-- 
CRITICAL: This section must contain ONLY requirements explicitly stated in assignment instructions.
Do NOT synthesize, infer, or add requirements not found in source materials.
If a requirement is ambiguous, note the ambiguity.
-->

### Deliverables
<!-- anchor: #deliverables -->

| Deliverable ID | Description | Format | Required |
|----------------|-------------|--------|----------|
| {ASSIGNMENT_ID}-DEL01 | {Deliverable description} | {PDF / Word / Other} | Yes |
| {ASSIGNMENT_ID}-DEL02 | {Deliverable description} | {Format} | Yes |
| {ASSIGNMENT_ID}-DEL03 | {Deliverable description} | {Format} | Optional |

### Content Requirements
<!-- anchor: #content-requirements -->

1. **{Requirement Category 1}**
   - {Specific requirement 1a}
   - {Specific requirement 1b}
   - {Specific requirement 1c}

2. **{Requirement Category 2}**
   - {Specific requirement 2a}
   - {Specific requirement 2b}

3. **{Requirement Category 3}**
   - {Specific requirement 3a}
   - {Specific requirement 3b}

### Formatting Requirements
<!-- anchor: #formatting-requirements -->

| Requirement | Specification |
|-------------|---------------|
| **Length** | {N pages / N words / N slides} |
| **Font** | {Font name, size} or Not specified |
| **Spacing** | {Single / Double / 1.5} or Not specified |
| **Margins** | {N inch} or Not specified |
| **Citation Style** | {APA / MLA / Chicago / Other} or Not specified |
| **File Format** | {PDF / Word / Other} |
| **File Naming** | {Required naming convention} or Not specified |
| **Header/Footer** | {Requirements} or Not specified |

### Structural Requirements
<!-- anchor: #structural-requirements -->

Required sections (if specified):

1. {Section 1 name} - {Brief description of expected content}
2. {Section 2 name} - {Brief description of expected content}
3. {Section 3 name} - {Brief description of expected content}
4. {Section 4 name} - {Brief description of expected content}

Or: No specific structure required / Structure at student discretion

---

## Submission
<!-- anchor: #submission -->

### Submission Method
<!-- anchor: #submission-method -->

| Field | Value |
|-------|-------|
| **Platform** | {Canvas / Gradescope / Email / In-class / Other} |
| **Submission Link** | {URL or location description} |
| **File Upload** | {Yes / No} |
| **Text Entry** | {Yes / No} |
| **Multiple Attempts** | {Yes (N attempts) / No / Unlimited} |

### Submission Checklist
<!-- anchor: #submission-checklist -->

Before submitting, verify:

- [ ] {Checklist item 1 - e.g., File saved in correct format}
- [ ] {Checklist item 2 - e.g., Name and ID included}
- [ ] {Checklist item 3 - e.g., All required sections complete}
- [ ] {Checklist item 4 - e.g., Citations properly formatted}
- [ ] {Checklist item 5 - e.g., File named according to convention}

---

## Grading
<!-- anchor: #grading -->

### Grading Criteria
<!-- anchor: #grading-criteria -->

<!-- Include rubric if provided in assignment instructions -->

| Criterion | Points | Description |
|-----------|--------|-------------|
| {Criterion 1} | {N pts} | {What earns full points} |
| {Criterion 2} | {N pts} | {What earns full points} |
| {Criterion 3} | {N pts} | {What earns full points} |
| {Criterion 4} | {N pts} | {What earns full points} |
| **Total** | **{N pts}** | |

Or: Rubric not provided in assignment instructions - check Canvas/LMS

### Grading Notes
<!-- anchor: #grading-notes -->

- {Any specific grading notes from instructor}
- {Emphasis areas}
- {Common deduction categories}

---

## Resources
<!-- anchor: #resources -->

### Required Resources
<!-- anchor: #required-resources -->

| Resource Type | Resource | Location |
|---------------|----------|----------|
| Reading | {Reading title/citation} | {M##-R## or filename} |
| Lecture | {Lecture title} | {M##-L## or filename} |
| Template | {Template name} | {Filename or link} |
| Data Set | {Data set name} | {Filename or link} |

### Recommended Resources
<!-- anchor: #recommended-resources -->

| Resource Type | Resource | Location |
|---------------|----------|----------|
| {Type} | {Resource description} | {Location} |
| {Type} | {Resource description} | {Location} |

### External Resources
<!-- anchor: #external-resources -->

- {External resource 1 with URL if applicable}
- {External resource 2 with URL if applicable}

---

## Clarifications and FAQs
<!-- anchor: #clarifications-faqs -->

### Instructor Clarifications
<!-- anchor: #instructor-clarifications -->

| Date (ISO) | Clarification |
|------------|---------------|
| {YYYY-MM-DD} | {Clarification text from instructor} |
| {YYYY-MM-DD} | {Clarification text from instructor} |

### Common Questions
<!-- anchor: #common-questions -->

**Q: {Common question 1}**
A: {Answer based on assignment instructions or instructor clarification}

**Q: {Common question 2}**
A: {Answer based on assignment instructions or instructor clarification}

---

## Ambiguities and Unknowns
<!-- anchor: #ambiguities-unknowns -->

<!-- 
Document any requirements that are unclear or missing from provided materials.
Agent should reference this section when answering questions about unclear requirements.
-->

| Item | Status | Notes |
|------|--------|-------|
| {Unclear requirement} | Not specified | {What is missing or ambiguous} |
| {Unclear requirement} | Awaiting clarification | {Question submitted to instructor} |
| {Unclear requirement} | Clarified | {See #instructor-clarifications} |

---

## Execution Support
<!-- anchor: #execution-support -->

### Suggested Approach
<!-- anchor: #suggested-approach -->

<!-- This section provides planning guidance, clearly marked as suggestions not requirements -->

**Note:** The following is a suggested approach based on assignment requirements. Actual approach should align with your learning style and instructor guidance.

1. **Phase 1: {Phase name}** ({Suggested timeframe})
   - {Task 1}
   - {Task 2}

2. **Phase 2: {Phase name}** ({Suggested timeframe})
   - {Task 1}
   - {Task 2}

3. **Phase 3: {Phase name}** ({Suggested timeframe})
   - {Task 1}
   - {Task 2}

### Time Estimate
<!-- anchor: #time-estimate -->

| Activity | Estimated Time |
|----------|----------------|
| Research/Reading | {N hours} |
| Drafting | {N hours} |
| Revision | {N hours} |
| Formatting/Finalization | {N hours} |
| **Total** | **{N hours}** |

**Assumption:** This estimate assumes {state any assumptions, e.g., prior familiarity with topic, completion of prerequisite readings}.

---

## Index References
<!-- anchor: #index-references -->

### Section Anchors in This File

| Section | Anchor ID |
|---------|-----------|
| Assignment Overview | #assignment-overview |
| Identification | #identification |
| Schedule | #schedule |
| Status | #status |
| Assignment Description | #assignment-description |
| Overview | #overview |
| Learning Objectives Assessed | #learning-objectives-assessed |
| Requirements | #requirements |
| Deliverables | #deliverables |
| Content Requirements | #content-requirements |
| Formatting Requirements | #formatting-requirements |
| Structural Requirements | #structural-requirements |
| Submission | #submission |
| Submission Method | #submission-method |
| Submission Checklist | #submission-checklist |
| Grading | #grading |
| Grading Criteria | #grading-criteria |
| Grading Notes | #grading-notes |
| Resources | #resources |
| Required Resources | #required-resources |
| Recommended Resources | #recommended-resources |
| External Resources | #external-resources |
| Clarifications and FAQs | #clarifications-faqs |
| Instructor Clarifications | #instructor-clarifications |
| Common Questions | #common-questions |
| Ambiguities and Unknowns | #ambiguities-unknowns |
| Execution Support | #execution-support |
| Suggested Approach | #suggested-approach |
| Time Estimate | #time-estimate |

### Entity IDs Defined in This File

| Entity Type | Entity ID | Title |
|-------------|-----------|-------|
| Assignment | {ASSIGNMENT_ID} | {Assignment Title} |
| Deliverable | {ASSIGNMENT_ID}-DEL01 | {Deliverable Title} |
| Deliverable | {ASSIGNMENT_ID}-DEL02 | {Deliverable Title} |

### Cross-References to Other Files

| Reference | Target File | Target Section |
|-----------|-------------|----------------|
| Due date authority | course_schedule.md | #assignment-calendar |
| Late policy | course_core.md | #late-work-policy |
| Grading weight | course_core.md | #grading-policy |
| Module content | {MODULE_ID}.module_manifest.md | #file-inventory |

---

## Change Log
<!-- anchor: #change-log -->

| Date (ISO) | Change Description |
|------------|-------------------|
| {YYYY-MM-DD} | Initial assignment record created |
| {YYYY-MM-DD} | {Description of update, e.g., Added instructor clarification} |

---

<!-- 
ASSIGNMENT RECORD TEMPLATE INSTRUCTIONS

PURPOSE:
This template creates a structured record of an individual assignment for 
retrieval support and execution guidance. It is a Working Memory File unless 
explicitly promoted to Grounded Knowledge by user instruction.

FILE NAMING:
Pattern: {assignment_id}.assignment_record.md
Examples: A03.assignment_record.md, ESSAY-02.assignment_record.md

ASSIGNMENT ID DERIVATION:
- If syllabus provides number: Use A{NN} or {TYPE}-{NN}
- If no number provided: Use {TYPE}-{NN}-{HASH} where HASH is first 4 chars 
  of SHA-256 hash of (title + due_date_iso), uppercased

TYPE CODES:
- QUIZ = Quiz
- EXAM = Exam  
- ESSAY = Essay
- PROJ = Project
- DISC = Discussion
- LAB = Lab
- HW = Homework
- A = Generic assignment

VALIDATION REQUIREMENTS:
1. assignment_id must match regex: ^[A-Z]+-?\d{2}(-[A-Z0-9]+)?$
2. All dates must use dual format (display_date + iso_date)
3. All times must use h:mm AM/PM format
4. TBD dates: display_date = "TBD", iso_date = null
5. All section anchors must be unique and lowercase-hyphenated

AUTHORITY LEVEL:
- Assignment records are Working Memory Files (Tier 6)
- They do NOT override Grounded Knowledge Files
- Due dates in course_schedule.md take precedence
- Policies in course_core.md take precedence

CRITICAL RULES:
1. Requirements section must contain ONLY explicitly stated requirements
2. Do NOT synthesize or infer requirements not in source materials
3. Document ambiguities in #ambiguities-unknowns section
4. Clearly mark suggested approaches as non-authoritative

AFTER CREATING:
1. Verify assignment_id is registered in INDEX
2. Cross-reference with course_schedule.md for date authority
3. Link to module manifest if assignment is module-associated
-->

---

**END OF TEMPLATE**