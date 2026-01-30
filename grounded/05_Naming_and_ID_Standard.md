# Naming and ID Standard

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Naming and identification specification  
**Date:** 2026-01-25  
**Phase:** 3  
**Status:** Definitive specification

---

## PURPOSE

This document defines the mandatory naming conventions and deterministic ID generation system for all files, entities, and references in the Course Assistant AI agent system. All Grounded Knowledge Files, Working Memory Files, and INDEX entries must follow these standards to ensure consistent, stable, and machine-parseable identifiers.

---

## NAMING PRINCIPLES

1. **Deterministic:** IDs must be derived consistently from available data (no random components)
2. **Stable:** IDs must not change unless the underlying entity fundamentally changes
3. **Human-readable:** IDs should be interpretable by humans when possible
4. **Machine-parseable:** IDs must match regex patterns for validation
5. **Collision-resistant:** IDs must be unique within their entity type
6. **No personal names:** IDs must not contain personal identifying information (except student first name "Josh")

---

## FILE NAMING CONVENTIONS

### Grounded Knowledge Files

**Pattern:** `{course_id}.{doc_type}.md`

**Regex:** `^[A-Z0-9\-]+\.(course_core|course_schedule|student_profile)\.md$`

**Components:**
- `{course_id}`: Course identifier (uppercase, alphanumeric, hyphens allowed)
- `{doc_type}`: One of: `course_core`, `course_schedule`, `student_profile`
- Extension: `.md` (Markdown)

**Examples:**
- `CARLSON-SCHOOL-2025-FA.course_core.md`
- `MGMT-5001-SEC01-2026-SP.course_schedule.md`
- `FIN-4200-2026-FA.student_profile.md`

**Validation rules:**
- ✓ Must contain exactly two dots (before doc_type and before extension)
- ✓ Course ID must be uppercase
- ✓ Doc type must be exactly one of the three allowed values
- ✓ Extension must be `.md`
- ✗ No spaces allowed
- ✗ No special characters except hyphens in course_id

---

### INDEX File

**Pattern:** `{course_id}.index.json`

**Regex:** `^[A-Z0-9\-]+\.index\.json$`

**Components:**
- `{course_id}`: Same as Grounded Knowledge Files
- Fixed string: `.index`
- Extension: `.json`

**Examples:**
- `CARLSON-SCHOOL-2025-FA.index.json`
- `MGMT-5001-SEC01-2026-SP.index.json`

---

### Module Package (Folder)

**Pattern:** `{module_id}/`

**Regex:** `^[A-Z0-9\-]+/$`

**Components:**
- `{module_id}`: Module identifier (see Module ID Standard below)
- Trailing slash indicates directory

**Examples:**
- `M01/`
- `CARLSON-FA25-M03/`
- `MODULE-02/`

---

### Module Package (ZIP)

**Pattern:** `{module_id}.zip`

**Regex:** `^[A-Z0-9\-]+\.zip$`

**Components:**
- `{module_id}`: Module identifier
- Extension: `.zip`

**Examples:**
- `M01.zip`
- `CARLSON-FA25-M03.zip`
- `MODULE-02.zip`

---

### Module Manifest (Inside Module Package)

**Pattern:** `{module_id}.module_manifest.md`

**Regex:** `^[A-Z0-9\-]+\.module_manifest\.md$`

**Components:**
- `{module_id}`: Must match parent module package name
- Fixed string: `.module_manifest`
- Extension: `.md`

**Examples:**
- `M01.module_manifest.md` (inside `M01/` or `M01.zip`)
- `CARLSON-FA25-M03.module_manifest.md` (inside `CARLSON-FA25-M03/` or `CARLSON-FA25-M03.zip`)

**Validation rule:**
- ✓ Module ID in manifest filename MUST match module package name exactly

---

### Curated Module File (Optional)

**Pattern:** `{course_id}.module_{module_id}_curated.md`

**Regex:** `^[A-Z0-9\-]+\.module_[A-Z0-9\-]+_curated\.md$`

**Components:**
- `{course_id}`: Course identifier
- Fixed string: `.module_`
- `{module_id}`: Module identifier
- Fixed string: `_curated`
- Extension: `.md`

**Examples:**
- `CARLSON-SCHOOL-2025-FA.module_M03_curated.md`
- `MGMT-5001-SEC01-2026-SP.module_MODULE-05_curated.md`

---

### Ad-Hoc Uploaded Files

**Pattern:** User-chosen (no strict pattern)

**Recommendation:**
- Use descriptive names
- Avoid spaces (use underscores or hyphens)
- Include file type in name if helpful
- Keep reasonable length (< 100 characters)

**Examples (good):**
- `Assignment_A03_Instructions.pdf`
- `Midterm-Study-Guide.docx`
- `reading-ch5-summary.txt`

**Examples (avoid):**
- `document (1).pdf` (non-descriptive)
- `final project instructions version 3 updated.docx` (spaces, verbose)

---

## ENTITY ID STANDARDS

### Course ID

**Purpose:** Uniquely identify the course and term for this agent build.

**Format:** `{INSTITUTION}-{COURSE}-{SECTION}-{TERM}`

**Pattern:** Uppercase, alphanumeric, hyphens separate components

**Components:**
- `{INSTITUTION}`: Institution abbreviation (optional but recommended)
- `{COURSE}`: Course number or code
- `{SECTION}`: Section identifier (optional)
- `{TERM}`: Term identifier (YYYY-TT format)

**Term format:**
- `YYYY-FA` = Fall
- `YYYY-SP` = Spring
- `YYYY-SU` = Summer
- `YYYY-WI` = Winter

**Examples:**
- `CARLSON-SCHOOL-2025-FA`
- `MGMT-5001-SEC01-2026-SP`
- `FIN-4200-2026-FA`
- `ACCT-2050-2025-SU`

**Derivation rule:**
If course materials provide:
- Institution name → Extract abbreviation (use official abbreviation if available)
- Course number/code → Use exactly as provided in syllabus
- Section → Include if multiple sections exist for the same course
- Term → Extract year and semester, convert to YYYY-TT format

**Regex:** `^[A-Z0-9\-]+$` (flexible to accommodate various institutional formats)

---

### Term ID

**Purpose:** Uniquely identify the academic term.

**Format:** `{YYYY}-{TT}`

**Components:**
- `{YYYY}`: Four-digit year
- `{TT}`: Two-letter term code (FA, SP, SU, WI)

**Examples:**
- `2025-FA`
- `2026-SP`
- `2026-SU`

**Regex:** `^(20\d{2})-(FA|SP|SU|WI)$`

**Derivation rule:**
1. Extract term from syllabus (e.g., "Fall 2025", "Spring 2026")
2. Convert to year (YYYY)
3. Convert semester to two-letter code:
   - Fall → FA
   - Spring → SP
   - Summer → SU
   - Winter → WI

---

### Module ID

**Purpose:** Uniquely identify a course module.

**Format:** `M{NN}` or `{COURSE}-{TERM}-M{NN}`

**Components:**
- `M`: Prefix indicating "Module"
- `{NN}`: Two-digit zero-padded module number (01, 02, ..., 10, 11, ...)
- Optional: Course and term prefix for disambiguation across courses

**Examples:**
- `M01` (simple format, sufficient for single-course agent)
- `M10`
- `CARLSON-FA25-M03` (extended format with course context)

**Regex:**  
- Simple: `^M\d{2}$`
- Extended: `^[A-Z0-9\-]+-M\d{2}$`

**Derivation rule:**
1. If syllabus provides module numbers → Use exactly as provided, zero-pad to 2 digits
2. If syllabus uses "Week 1", "Week 2" → Convert to M01, M02, ...
3. If syllabus uses "Unit A", "Unit B" → Map alphabetically (A→01, B→02, ...)
4. If no module structure → Create sequential IDs starting with M01 based on course schedule

**Stability:** Module IDs should NOT change mid-term. Once assigned, module IDs are permanent for the term.

---

### Assignment ID

**Purpose:** Uniquely identify a course assignment.

**Format:** `A{NN}` or `{TYPE}-{NN}` or `{TYPE}-{TITLE-HASH}`

**Components:**
- `A`: Prefix indicating "Assignment"
- `{TYPE}`: Assignment type code (optional)
- `{NN}`: Two-digit zero-padded assignment number
- `{TITLE-HASH}`: Short hash of assignment title (fallback when no number provided)

**Assignment type codes (optional):**
- `QUIZ` = Quiz
- `EXAM` = Exam
- `ESSAY` = Essay assignment
- `PROJ` = Project
- `DISC` = Discussion
- `LAB` = Lab assignment
- `HW` = Homework

**Examples:**
- `A01` (first assignment, generic)
- `A10` (tenth assignment)
- `QUIZ-01` (first quiz)
- `EXAM-MIDTERM` (midterm exam)
- `PROJ-FINAL` (final project)
- `ESSAY-02-A7F3` (second essay, with hash suffix for disambiguation)

**Regex:**
- Simple: `^A\d{2}$`
- Typed: `^[A-Z]+-\d{2}$`
- Hashed: `^[A-Z]+-[A-Z0-9\-]+$`

**Derivation rule (when syllabus provides assignment number):**
1. Extract assignment type and number from syllabus
2. Zero-pad number to 2 digits
3. Use format `{TYPE}-{NN}` or `A{NN}`

**Derivation rule (when syllabus provides ONLY title/type/due date):**
1. Extract assignment type (quiz, exam, essay, etc.)
2. Count assignments of same type to generate sequential number
3. If disambiguation needed → Append 4-character hash of (title + due_date)
4. Use format `{TYPE}-{NN}` or `{TYPE}-{TITLE-HASH}`

**Hash generation (when needed):**
```
hash_input = f"{assignment_title}_{due_date_iso}"
hash_suffix = hashlib.sha256(hash_input.encode()).hexdigest()[:4].upper()
assignment_id = f"{type_code}-{seq_num:02d}-{hash_suffix}"
```

**Example:**
- Assignment title: "Marketing Analysis Essay"
- Due date: 2026-02-15
- Type: ESSAY
- Sequence: 02 (second essay)
- Hash input: `Marketing Analysis Essay_2026-02-15`
- Hash suffix: `A7F3` (first 4 chars of SHA-256 hash, uppercased)
- Assignment ID: `ESSAY-02-A7F3`

**Stability:** Assignment IDs should NOT change after initial creation unless the assignment is fundamentally redefined.

---

### Exam ID

**Purpose:** Uniquely identify a course exam.

**Format:** `EXAM-{NAME}` or `{EXAM-TYPE}`

**Components:**
- Fixed prefix: `EXAM-`
- `{NAME}`: Exam name (MIDTERM, FINAL, etc.)
- Or standalone: `MIDTERM`, `FINAL`, `EXAM-01`, etc.

**Examples:**
- `EXAM-MIDTERM`
- `EXAM-FINAL`
- `MIDTERM` (simplified)
- `FINAL` (simplified)
- `EXAM-01` (numbered exams)

**Regex:** `^(EXAM-)?[A-Z0-9\-]+$`

**Derivation rule:**
1. If syllabus uses "Midterm", "Final" → Use `MIDTERM`, `FINAL`
2. If syllabus uses "Exam 1", "Exam 2" → Use `EXAM-01`, `EXAM-02`
3. If syllabus uses custom name → Convert to uppercase, replace spaces with hyphens

**Examples:**
- "Midterm Exam" → `MIDTERM`
- "Final Examination" → `FINAL`
- "Exam 1" → `EXAM-01`
- "Unit Test 3" → `EXAM-UNIT-03`

---

### Reading ID

**Purpose:** Uniquely identify a course reading assignment.

**Format:** `R{NN}` or `M{NN}-R{NN}`

**Components:**
- `R`: Prefix indicating "Reading"
- `{NN}`: Two-digit zero-padded reading number
- Optional: `M{NN}-` prefix to indicate module association

**Examples:**
- `R01` (first reading, global sequence)
- `R10` (tenth reading)
- `M02-R01` (first reading in Module 2)
- `M05-R03` (third reading in Module 5)

**Regex:**
- Simple: `^R\d{2}$`
- Module-scoped: `^M\d{2}-R\d{2}$`

**Derivation rule:**
1. If readings are numbered globally → Use `R{NN}`
2. If readings are numbered per module → Use `M{NN}-R{NN}`
3. Sequence number based on order in syllabus/schedule

---

### Discussion ID

**Purpose:** Uniquely identify a course discussion assignment.

**Format:** `D{NN}` or `M{NN}-D{NN}`

**Components:**
- `D`: Prefix indicating "Discussion"
- `{NN}`: Two-digit zero-padded discussion number
- Optional: `M{NN}-` prefix to indicate module association

**Examples:**
- `D01` (first discussion)
- `D05` (fifth discussion)
- `M03-D01` (first discussion in Module 3)

**Regex:**
- Simple: `^D\d{2}$`
- Module-scoped: `^M\d{2}-D\d{2}$`

**Derivation rule:** Same as Reading ID

---

### Lecture ID (Optional)

**Purpose:** Uniquely identify a course lecture.

**Format:** `L{NN}` or `M{NN}-L{NN}`

**Components:**
- `L`: Prefix indicating "Lecture"
- `{NN}`: Two-digit zero-padded lecture number
- Optional: `M{NN}-` prefix to indicate module association

**Examples:**
- `L01`
- `M02-L01` (first lecture in Module 2)

**Regex:**
- Simple: `^L\d{2}$`
- Module-scoped: `^M\d{2}-L\d{2}$`

---

### Milestone ID (For Group Projects)

**Purpose:** Uniquely identify a group project milestone.

**Format:** `{PROJECT_ID}-MS{NN}` or `MS{NN}`

**Components:**
- `{PROJECT_ID}`: Group project identifier (optional)
- `MS`: Prefix indicating "Milestone"
- `{NN}`: Two-digit zero-padded milestone number

**Examples:**
- `MS01` (first milestone, single project)
- `MS03` (third milestone)
- `PROJ-FINAL-MS01` (first milestone of final project)
- `GP01-MS02` (second milestone of group project 1)

**Regex:**
- Simple: `^MS\d{2}$`
- Project-scoped: `^[A-Z0-9\-]+-MS\d{2}$`

**Derivation rule:**
1. If single group project in course → Use `MS{NN}`
2. If multiple group projects → Use `{PROJECT_ID}-MS{NN}`
3. Sequence milestones in chronological order

---

### Group Project ID

**Purpose:** Uniquely identify a group project.

**Format:** `GP{NN}` or `PROJ-{NAME}`

**Components:**
- `GP`: Prefix indicating "Group Project"
- `{NN}`: Two-digit zero-padded project number
- Or `PROJ-{NAME}`: Project name in uppercase

**Examples:**
- `GP01` (first group project)
- `PROJ-FINAL` (final group project)
- `PROJ-MARKETING-PLAN` (named project)

**Regex:** `^(GP\d{2}|PROJ-[A-Z0-9\-]+)$`

**Derivation rule:**
1. If syllabus numbers projects → Use `GP{NN}`
2. If syllabus names project (e.g., "Final Project") → Use `PROJ-{NAME}`
3. Convert name to uppercase, replace spaces with hyphens

---

### Deliverable ID (For Assignments/Projects)

**Purpose:** Uniquely identify a specific deliverable within an assignment or project.

**Format:** `{ASSIGNMENT_ID}-DEL{NN}` or `DEL{NN}`

**Components:**
- `{ASSIGNMENT_ID}`: Parent assignment or project ID
- `DEL`: Prefix indicating "Deliverable"
- `{NN}`: Two-digit zero-padded deliverable number

**Examples:**
- `A03-DEL01` (first deliverable of Assignment 3)
- `PROJ-FINAL-DEL02` (second deliverable of final project)
- `MS01-DEL01` (deliverable associated with milestone 1)

**Regex:** `^[A-Z0-9\-]+-DEL\d{2}$`

**Derivation rule:**
1. Identify parent assignment/project/milestone
2. Number deliverables sequentially
3. Use format `{PARENT_ID}-DEL{NN}`

---

## SECTION ANCHOR ID STANDARDS

**Purpose:** Provide stable, unique anchors for linking to specific sections within Markdown files.

**Format:** `#{section-name}`

**Pattern:** Lowercase, hyphens separate words, no spaces, no special characters

**Generation rule:**
1. Take section header text
2. Convert to lowercase
3. Replace spaces with hyphens
4. Remove special characters (except hyphens)
5. Prefix with `#`

**Examples:**
- Header: `## Course Identification` → Anchor: `#course-identification`
- Header: `### Grading Policy: Components and Weights` → Anchor: `#grading-policy-components-and-weights`
- Header: `## Assignment Calendar` → Anchor: `#assignment-calendar`

**Uniqueness requirement:**
- All section anchors within a file MUST be unique
- If duplication would occur, append `-1`, `-2`, etc.

**Example (handling duplicates):**
- First occurrence: `## Overview` → `#overview`
- Second occurrence: `## Overview` (in different section) → `#overview-1`

**Validation:**
- ✓ Must start with `#`
- ✓ Lowercase only
- ✓ Hyphens separate words
- ✓ No spaces
- ✓ No special characters except hyphens
- ✓ Unique within file

**Regex:** `^#[a-z0-9\-]+$`

---

## METADATA FIELD ID STANDARDS

### Required Metadata Fields (All Grounded Knowledge Files)

**Field:** `course_id`  
**Format:** As defined in Course ID Standard above  
**Example:** `CARLSON-SCHOOL-2025-FA`

**Field:** `term_id`  
**Format:** As defined in Term ID Standard above  
**Example:** `2025-FA`

**Field:** `doc_type`  
**Format:** One of: `course_core`, `course_schedule`, `student_profile`, `index`, `module_manifest`, `curated_module`  
**Example:** `course_schedule`

**Field:** `last_updated`  
**Format:** `YYYY-MM-DD` (ISO 8601 date only, no time)  
**Example:** `2026-01-25`

**Field:** `timezone`  
**Format:** IANA timezone name or two-letter abbreviation  
**Examples:** `America/Chicago`, `CT`  
**Preference:** Use IANA name for precision

**Field:** `source_files` (optional)  
**Format:** Comma-separated list of original source filenames  
**Example:** `syllabus_mgmt5001_fa25.pdf, schedule_fa25.xlsx`

---

### Optional Metadata Fields

**Field:** `index_version` (index.json only)  
**Format:** Semantic versioning (optional) or simple incrementing  
**Examples:** `1.0.0`, `v3`, `2026-01-25` (date-based)

**Field:** `change_log` (optional, all files)  
**Format:** Free text or structured list  
**Example:**
```
- 2026-01-25: Updated Assignment A03 due date
- 2026-01-20: Added Module 5
```

---

## CROSS-REFERENCE FORMAT

**Purpose:** Reference entities across files in INDEX and within Grounded Knowledge Files.

**Format:** `{filename}#{section_id}` or `{filename}#{section_id}({entity_id})`

**Components:**
- `{filename}`: Full filename including extension
- `#`: Anchor separator
- `{section_id}`: Section anchor ID
- `()`: Optional parentheses for entity ID
- `{entity_id}`: Entity identifier

**Examples:**
- `course_core.md#grading-policy`
- `course_schedule.md#assignment-calendar(A03)`
- `student_profile.md#group-project-context(GP01)`
- `M03/Module_03_Lecture.pptx` (file reference without section)

**Regex:** `^[A-Za-z0-9_\-\.]+#[a-z0-9\-]+(\([A-Z0-9\-]+\))?$`

**Validation:**
- ✓ Filename exists
- ✓ Section anchor exists in file
- ✓ Entity ID exists in section (if specified)

---

## NAMING CONFLICT RESOLUTION

### Conflict Scenario 1: Module ID Collision

**Example:** Module 3 and Module 03 both map to `M03`

**Resolution:**
- Always zero-pad to 2 digits
- Module 3 → `M03`
- Module 03 → `M03` (same ID, no conflict)

---

### Conflict Scenario 2: Assignment ID Collision

**Example:** Two assignments both titled "Essay" due on different dates

**Resolution:**
- Use sequential numbering: `ESSAY-01`, `ESSAY-02`
- If ambiguous, append hash: `ESSAY-01-A7F3`, `ESSAY-02-B8E4`

---

### Conflict Scenario 3: Section Anchor Collision

**Example:** Two sections with same title "Overview"

**Resolution:**
- First occurrence: `#overview`
- Second occurrence: `#overview-1`
- Third occurrence: `#overview-2`

---

## VALIDATION REGEX SUMMARY

| Entity Type | Regex Pattern |
|-------------|---------------|
| Course ID | `^[A-Z0-9\-]+$` |
| Term ID | `^(20\d{2})-(FA\|SP\|SU\|WI)$` |
| Module ID (simple) | `^M\d{2}$` |
| Module ID (extended) | `^[A-Z0-9\-]+-M\d{2}$` |
| Assignment ID | `^[A-Z]+-?\d{2}(-[A-Z0-9]+)?$` |
| Exam ID | `^(EXAM-)?[A-Z0-9\-]+$` |
| Reading ID | `^(M\d{2}-)?R\d{2}$` |
| Discussion ID | `^(M\d{2}-)?D\d{2}$` |
| Milestone ID | `^([A-Z0-9\-]+-)?MS\d{2}$` |
| Section Anchor | `^#[a-z0-9\-]+$` |
| Filename (GK) | `^[A-Z0-9\-]+\.(course_core\|course_schedule\|student_profile)\.md$` |
| Filename (INDEX) | `^[A-Z0-9\-]+\.index\.json$` |

---

## EXAMPLES: COMPLETE FILE AND ENTITY SET

**Course:** MGMT 5001, Section 01, Fall 2025  
**Institution:** Carlson School

### File Names

- `MGMT-5001-SEC01-2025-FA.course_core.md`
- `MGMT-5001-SEC01-2025-FA.course_schedule.md`
- `MGMT-5001-SEC01-2025-FA.student_profile.md`
- `MGMT-5001-SEC01-2025-FA.index.json`

### Entity IDs

- **course_id:** `MGMT-5001-SEC01-2025-FA`
- **term_id:** `2025-FA`
- **Modules:** `M01`, `M02`, `M03`, ..., `M12`
- **Assignments:** `A01`, `A02`, `QUIZ-01`, `EXAM-MIDTERM`, `PROJ-FINAL`
- **Exams:** `MIDTERM`, `FINAL`
- **Readings:** `M01-R01`, `M01-R02`, `M02-R01`
- **Discussions:** `D01`, `D02`, `D03`
- **Group Project:** `PROJ-FINAL`
- **Milestones:** `PROJ-FINAL-MS01`, `PROJ-FINAL-MS02`, `PROJ-FINAL-MS03`

### Section Anchors

- `#metadata`
- `#course-identification`
- `#grading-policy`
- `#assignment-calendar`
- `#module-sequence`
- `#group-project-context`

### Cross-References

- `course_schedule.md#assignment-calendar(A03)`
- `course_core.md#grading-policy`
- `student_profile.md#group-project-context(PROJ-FINAL)`

---

**END OF DOCUMENT**