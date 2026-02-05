# Module Package Template

**Filename Pattern:** `{course_id}_M{NN}.manifest.md`  
**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.manifest\.md$`  
**Authority Tier:** 5 (Module content inventory)  
**Example Filename:** `MKTG6051_M03.manifest.md`

**Purpose:** Inventories all files in a module package and provides module overview information. This is a Working Memory File that supports assignment execution.

**Module Content File Naming Convention:**
- Format: `{CourseID}_M{ModuleNumber}.{TypeCode}_{short-description}.{extension}`
- Type Codes: `.A` (Assignment), `.L` (Lecture), `.R` (Resource), `.B` (Business case)
- Example: `MKTG6051_M02.L_survey-design.pptx`

---

## Metadata
<!-- anchor: #metadata -->

| Field | Value |
|-------|-------|
| **course_id** | `{COURSE_ID}` |
| **term_id** | `{YYYY}-{TT}` |
| **course_run_id** | `{COURSE_ID}-{YYYY}-{TT}` |
| **module_id** | {MODULE_ID} |
| **module_title** | {Module N: Topic Title} |
| **doc_type** | module_manifest |
| **last_updated** | {YYYY-MM-DD} |

---

## Module Overview
<!-- anchor: #module-overview -->

{Brief 2-3 sentence description of what this module covers and why it matters.}

### Learning Objectives

By the end of this module, you should be able to:

1. {Learning objective 1 - use action verbs: analyze, evaluate, create, apply, etc.}
2. {Learning objective 2}
3. {Learning objective 3}
4. {Learning objective 4 - OPTIONAL}

### Estimated Time

| Activity | Estimated Time |
|----------|----------------|
| Lectures/Videos | {N hours} |
| Readings | {N hours} |
| Assignments | {N hours} |
| **Total** | **{N hours}** |

---

## File Inventory
<!-- anchor: #file-inventory -->

**File Naming Convention:** `{CourseID}_M{NN}.{TypeCode}_{short-description}.{extension}`

**Type Codes:**
- `.A` = Assignment (instructions, rubric, template, submission)
- `.L` = Lecture (slides, notes, video transcripts)
- `.R` = Resource (articles, books, references)
- `.B` = Business case

| File Path | Type Code | File Type | Description | Required |
|-----------|-----------|-----------|-------------|----------|
| {course_id}_M{NN}.manifest.md | - | .md | This manifest file | Yes |
| {course_id}_M{NN}.L_{description}.pptx | L | .pptx | Lecture slides | Yes |
| {course_id}_M{NN}.A_{description}.pdf | A | .pdf | Assignment instructions | Yes |
| {course_id}_M{NN}.R_{description}.pdf | R | .pdf | Reading/resource | No |
| {course_id}_M{NN}.B_{description}.docx | B | .docx | Business case | No |

**Example Files (MKTG6051 Module 02):**
| File Path | Type Code | File Type | Description | Required |
|-----------|-----------|-----------|-------------|----------|
| MKTG6051_M02.manifest.md | - | .md | This manifest file | Yes |
| MKTG6051_M02.L_survey-design.pptx | L | .pptx | Lecture slides on survey design | Yes |
| MKTG6051_M02.A_chapter-questions.md | A | .md | Assignment questions | Yes |
| MKTG6051_M02.R_demand-and-supply.pdf | R | .pdf | Demand and supply article | No |
| MKTG6051_M02.B_airbus-v-boeing.docx | B | .docx | Airbus vs Boeing case study | No |

**Allowed File Types**: `.md`, `.txt`, `.csv`, `.xlsx`, `.pdf`, `.pptx`, `.docx`

**Note:** All files in the module package must be listed in this inventory. Files not in this inventory will not be indexed.

---

## Assignment Links
<!-- anchor: #assignment-links -->

{References to assignments associated with this module. Due dates are authoritative in course_schedule.md.}

| Assignment ID | Title | Type | Due Date Reference |
|---------------|-------|------|-------------------|
| {A##} | {Assignment title} | {individual/quiz/discussion/exam/group/presentation} | course_schedule.md#assignment-calendar |

---

## Notes
<!-- anchor: #notes -->

{Optional: Instructor notes or guidance for this module.}

---

## Index References
<!-- anchor: #index-references -->

This file contains the following sections indexed for retrieval:

| Section Anchor | Section Title |
|----------------|---------------|
| #metadata | Metadata |
| #module-overview | Module Overview |
| #file-inventory | File Inventory |
| #assignment-links | Assignment Links |
| #notes | Notes |
| #index-references | Index References |

---

## Template Validation Checklist

Before finalizing module manifest, verify:

- [ ] course_id matches naming convention (e.g., MKTG6051, MGMT6022)
- [ ] term_id follows YYYY-TT format (e.g., 2026-SP)
- [ ] course_run_id follows pattern: {course_id}-{term_id}
- [ ] module_id matches regex: ^(M\d{2}|GK)$
- [ ] Filename follows pattern: {course_id}_M{NN}.manifest.md
- [ ] All files follow naming convention: {CourseID}_M{NN}.{TypeCode}_{description}.{ext}
- [ ] All file types are allowed: .md, .txt, .csv, .xlsx, .pdf, .pptx, .docx
- [ ] Type codes are valid: A (Assignment), L (Lecture), R (Resource), B (Business case)
- [ ] Assignment IDs match entries in course_schedule.md
- [ ] No dates are listed (dates are in course_schedule.md only)

---

<!--
MODULE PACKAGE TEMPLATE INSTRUCTIONS

FILE NAMING CONVENTION:
Format: {CourseID}_M{ModuleNumber}.{TypeCode}_{short-description}.{extension}

Type Codes:
- .A = Assignment (instructions, rubric, template, submission)
- .L = Lecture (slides, notes, video transcripts)
- .R = Resource (article, book, video transcript, etc.)
- .B = Business case

Examples:
- MKTG6051_M01.A_chapter-12-questions.md
- MKTG6051_M02.L_survey-design.pptx
- MKTG6051_M02.R_demand-and-supply.pdf
- MKTG6051_M02.B_airbus-v-boeing.docx
- MKTG6051_GK_syllabus.pdf

FOLDER/ZIP NAMING:
- Manifest file: {course_id}_M{NN}.manifest.md (e.g., MKTG6051_M03.manifest.md)
- Folder name: {course_id}_M{NN}/ (e.g., MKTG6051_M03/)
- ZIP name (if zipped): {course_id}_M{NN}.zip (e.g., MKTG6051_M03.zip)

ALLOWED FILE TYPES:
- .md (Markdown documentation)
- .txt (Plain text)
- .csv (Spreadsheet data)
- .xlsx (Excel spreadsheet)
- .pdf (Documents)
- .pptx (PowerPoint presentations)
- .docx (Word documents)

AUTHORITY LEVEL:
- Module manifests are Tier 5 in authority hierarchy
- They do NOT override Grounded Knowledge Files
- Dates in course_schedule.md take precedence

REQUIRED CONTENTS:
- This manifest file ({course_id}_M{NN}.manifest.md)

AFTER UPLOADING:
1. Prompt agent to scan and verify module contents
2. Update INDEX with new module files
3. Verify all entity IDs are registered in INDEX
-->

---

**END OF TEMPLATE**
