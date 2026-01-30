# Module Package Template

---

## Metadata
<!-- REQUIRED: Complete all fields before use -->

| Field | Value |
|-------|-------|
| **module_id** | {MODULE_ID} |
| **course_id** | {COURSE_ID} |
| **term_id** | {TERM_ID} |
| **doc_type** | module_manifest |
| **last_updated** | {YYYY-MM-DD} |
| **timezone** | America/Chicago |
| **source_files** | {comma-separated list of original source filenames} |

---

## Module Overview
<!-- anchor: #module-overview -->

### Basic Information
<!-- anchor: #basic-information -->

| Field | Value |
|-------|-------|
| **Module ID** | {MODULE_ID} |
| **Module Title** | {Module N: Topic Title} |
| **Module Number** | {NN} |
| **Start Date (display)** | {DayOfWeek, Mon DD, YYYY} |
| **Start Date (ISO)** | {YYYY-MM-DD} |
| **End Date (display)** | {DayOfWeek, Mon DD, YYYY} |
| **End Date (ISO)** | {YYYY-MM-DD} |
| **Duration** | {N days / N week(s)} |
| **Status** | {Not Started / In Progress / Completed} |

### Module Description
<!-- anchor: #module-description -->

{Brief 2-3 sentence description of what this module covers and why it matters.}

---

## Learning Objectives
<!-- anchor: #learning-objectives -->

By the end of this module, you should be able to:

1. {Learning objective 1 - use action verbs: analyze, evaluate, create, apply, etc.}
2. {Learning objective 2}
3. {Learning objective 3}
4. {Learning objective 4 - OPTIONAL}
5. {Learning objective 5 - OPTIONAL}

---

## Dependencies
<!-- anchor: #dependencies -->

### Prerequisite Modules
<!-- anchor: #prerequisite-modules -->

| Module ID | Module Title | Required/Recommended |
|-----------|--------------|----------------------|
| {M##} | {Module Title} | Required |
| {M##} | {Module Title} | Recommended |
| None | N/A | N/A |

### Required Prior Knowledge
<!-- anchor: #required-prior-knowledge -->

- {Concept or skill required before starting this module}
- {Another prerequisite concept}
- None specified

---

## File Inventory
<!-- anchor: #file-inventory -->

### Summary
<!-- anchor: #inventory-summary -->

| Category | Count |
|----------|-------|
| Total Files | {N} |
| Lecture Materials | {N} |
| Readings | {N} |
| Assignment Documents | {N} |
| Supplementary Resources | {N} |

### Lecture Materials
<!-- anchor: #lecture-materials -->

| File ID | Filename | File Type | Description | Required |
|---------|----------|-----------|-------------|----------|
| {MODULE_ID}-LEC-01 | {filename.pptx} | PowerPoint | {Brief description} | Yes |
| {MODULE_ID}-LEC-02 | {filename.pdf} | PDF | {Brief description} | Yes |
| {MODULE_ID}-VID-01 | {filename.mp4} | Video | {Brief description, duration} | Yes |

### Readings
<!-- anchor: #readings -->

| Reading ID | Filename | File Type | Citation/Title | Pages | Required |
|------------|----------|-----------|----------------|-------|----------|
| {M##-R01} | {filename.pdf} | PDF | {Author (Year), Title} | {pp. X-Y or All} | Yes |
| {M##-R02} | {filename.pdf} | PDF | {Author (Year), Title} | {pp. X-Y or All} | Yes |
| {M##-R03} | {External link} | Web | {Article Title} | N/A | Recommended |

### Assignment Documents
<!-- anchor: #assignment-documents -->

| Assignment ID | Filename | File Type | Description | Due Date (ISO) |
|---------------|----------|-----------|-------------|----------------|
| {A##} | {Assignment_Instructions.pdf} | PDF | {Assignment title} | {YYYY-MM-DD} |
| {QUIZ-##} | {Quiz_Study_Guide.pdf} | PDF | {Quiz description} | {YYYY-MM-DD} |

### Supplementary Resources
<!-- anchor: #supplementary-resources -->

| Resource ID | Filename | File Type | Description | Required |
|-------------|----------|-----------|-------------|----------|
| {MODULE_ID}-SUP-01 | {filename.xlsx} | Excel | {Template/tool description} | Optional |
| {MODULE_ID}-SUP-02 | {filename.pdf} | PDF | {Example/case study} | Optional |

---

## Topics Covered
<!-- anchor: #topics-covered -->

### Primary Topics
<!-- anchor: #primary-topics -->

1. **{Topic 1 Title}**
   - {Subtopic 1a}
   - {Subtopic 1b}
   - {Subtopic 1c}

2. **{Topic 2 Title}**
   - {Subtopic 2a}
   - {Subtopic 2b}

3. **{Topic 3 Title}**
   - {Subtopic 3a}
   - {Subtopic 3b}

### Key Concepts
<!-- anchor: #key-concepts -->

- **{Concept 1}**: {Brief definition or explanation}
- **{Concept 2}**: {Brief definition or explanation}
- **{Concept 3}**: {Brief definition or explanation}

### Key Frameworks/Models
<!-- anchor: #key-frameworks -->

- **{Framework 1 Name}**: {Brief description of framework and its use}
- **{Framework 2 Name}**: {Brief description of framework and its use}

---

## Schedule Integration
<!-- anchor: #schedule-integration -->

### Module Timeline
<!-- anchor: #module-timeline -->

| Day | Date (display) | Date (ISO) | Activities |
|-----|----------------|------------|------------|
| Day 1 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Lecture 1, Reading R01} |
| Day 2 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Reading R02, Discussion opens} |
| Day 3 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Lecture 2} |
| Day 4 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Assignment work time} |
| Day 5 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Discussion closes, Assignment due} |

### Associated Deadlines
<!-- anchor: #associated-deadlines -->

| Entity ID | Entity Type | Title | Due Date (display) | Due Date (ISO) | Due Time |
|-----------|-------------|-------|-------------------|----------------|----------|
| {A##} | Assignment | {Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} |
| {D##} | Discussion | {Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} |
| {M##-R01} | Reading | {Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | Before class |

---

## Connections to Course
<!-- anchor: #connections-to-course -->

### Related Course Objectives
<!-- anchor: #related-course-objectives -->

This module supports the following course-level learning objectives:

- {Course objective 1 from course_core.md}
- {Course objective 2 from course_core.md}

### Connection to Other Modules
<!-- anchor: #connection-to-other-modules -->

| Relationship | Module ID | Module Title | Description |
|--------------|-----------|--------------|-------------|
| Builds on | {M##} | {Title} | {How this module builds on prior content} |
| Prepares for | {M##} | {Title} | {How this module prepares for future content} |
| Related to | {M##} | {Title} | {Thematic or conceptual connection} |

### Connection to Assignments
<!-- anchor: #connection-to-assignments -->

| Assignment ID | Assignment Title | Relationship |
|---------------|------------------|--------------|
| {A##} | {Title} | Primary (directly assessed) |
| {PROJ-##} | {Title} | Contributing (supports project work) |

---

## Index References
<!-- anchor: #index-references -->

### Section Anchors in This File

| Section | Anchor ID |
|---------|-----------|
| Module Overview | #module-overview |
| Basic Information | #basic-information |
| Module Description | #module-description |
| Learning Objectives | #learning-objectives |
| Dependencies | #dependencies |
| Prerequisite Modules | #prerequisite-modules |
| Required Prior Knowledge | #required-prior-knowledge |
| File Inventory | #file-inventory |
| Inventory Summary | #inventory-summary |
| Lecture Materials | #lecture-materials |
| Readings | #readings |
| Assignment Documents | #assignment-documents |
| Supplementary Resources | #supplementary-resources |
| Topics Covered | #topics-covered |
| Primary Topics | #primary-topics |
| Key Concepts | #key-concepts |
| Key Frameworks | #key-frameworks |
| Schedule Integration | #schedule-integration |
| Module Timeline | #module-timeline |
| Associated Deadlines | #associated-deadlines |
| Connections to Course | #connections-to-course |
| Related Course Objectives | #related-course-objectives |
| Connection to Other Modules | #connection-to-other-modules |
| Connection to Assignments | #connection-to-assignments |

### Entity IDs Defined in This File

| Entity Type | Entity ID | Title |
|-------------|-----------|-------|
| Module | {MODULE_ID} | {Module Title} |
| Reading | {M##-R01} | {Reading Title} |
| Reading | {M##-R02} | {Reading Title} |
| Lecture | {M##-L01} | {Lecture Title} |

### Cross-References to Other Files

| Reference | Target File | Target Section |
|-----------|-------------|----------------|
| Course schedule dates | course_schedule.md | #module-sequence |
| Assignment details | course_schedule.md | #assignment-calendar |
| Course objectives | course_core.md | #learning-objectives |

---

## Notes
<!-- anchor: #notes -->

### Instructor Notes (if provided)
<!-- anchor: #instructor-notes -->

{Any instructor-provided guidance or tips for this module}

### Student Notes
<!-- anchor: #student-notes -->

{Space for student to add personal notes, questions, or observations}

---

## Change Log
<!-- anchor: #change-log -->

| Date (ISO) | Change Description |
|------------|-------------------|
| {YYYY-MM-DD} | Initial module package created |
| {YYYY-MM-DD} | {Description of update} |

---

<!-- 
MODULE PACKAGE TEMPLATE INSTRUCTIONS

FILE NAMING:
- Manifest file: {module_id}.module_manifest.md (e.g., M03.module_manifest.md)
- Folder name: {module_id}/ (e.g., M03/)
- ZIP name (if zipped): {module_id}.zip (e.g., M03.zip)

VALIDATION REQUIREMENTS:
1. module_id must match regex: ^M\d{2}$ (simple) or ^[A-Z0-9\-]+-M\d{2}$ (extended)
2. All dates must use dual format (display_date + iso_date)
3. All times must use h:mm AM/PM format
4. All section anchors must be unique and lowercase-hyphenated
5. All entity IDs must follow Naming and ID Standard
6. File inventory must list ALL files in the module package

AUTHORITY LEVEL:
- Module manifests are Tier 5 in authority hierarchy
- Module manifests describe what SHOULD be in the package
- They do NOT override Grounded Knowledge Files
- Dates in course_schedule.md take precedence over dates listed here

REQUIRED CONTENTS:
- This manifest file ({module_id}.module_manifest.md)
- At least one lecture material OR reading
- Assignment instructions (if assignment is associated with this module)

OPTIONAL CONTENTS:
- Supplementary resources
- Video files
- Templates or tools
- Case studies or examples

AFTER UPLOADING:
1. Prompt agent to scan and verify module contents
2. Update INDEX with new module files
3. Verify all entity IDs are registered in INDEX
-->

---

**END OF TEMPLATE**