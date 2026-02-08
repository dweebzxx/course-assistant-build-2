# Naming and ID Standard - Updated

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Naming and identification specification  
**Date:** 2026-01-25  
**Phase:** 3  
**Status:** Definitive specification

---

## PURPOSE

This document defines the mandatory naming conventions and deterministic ID generation system for all files, entities, and references in the Course Assistant AI agent system. All Grounded Knowledge Files, Working Memory Files, and INDEX entries must follow these standards to ensure consistent, stable, and machine-parseable identifiers.

---

## DEFINITIONS (NON-NEGOTIABLE)

### Course ID (`course_id`)
**What it is:** The official course code only, e.g. `MGMT6022`.

**What it is NOT:**
- Not a school name, department name, or institution label.
  - Example: `CARLSON-SCHOOL` is NOT a course id.
- Not a term or year.
  - Do not embed `2026`, `FA`, `SP`, `Fall`, `Spring`, etc.

**Canonical format:** `{DEPT}{NUMBER}`  
- `DEPT`: 2–10 uppercase letters (no hyphens)
- `NUMBER`: 3–5 digits
- Example: `MGMT6022`, `FINA4011`, `ACCT2050`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}$`

**Derivation rule:**
1. Use the exact course code as printed in the syllabus or LMS (after normalization).
2. Normalize by removing spaces/hyphens between dept and number and uppercasing.
   - `MGMT 6022` → `MGMT6022`
   - `MGMT-6022` → `MGMT6022`

---

### Term ID (`term_id`)
**What it is:** The academic term for this course instance.

**Format:** `{YYYY}-{TT}` where `TT ∈ {FA, SP, SU, WI}`  
**Examples:** `2026-SP`, `2025-FA`  
**Regex:** `^(20[0-9]{2})-(FA|SP|SU|WI)$`

**Derivation rule:**
1. Extract term from syllabus (e.g., “Spring 2026”).
2. Convert:
   - Fall → FA
   - Spring → SP
   - Summer → SU
   - Winter → WI

---

### Course Run ID (`course_run_id`) (required when term matters)
**Purpose:** A deterministic identifier for “this course in this term.”

**Format:** `{course_id}-{term_id}`  
**Example:** `MGMT6022-2026-SP`  
**Regex:** `^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA|SP|SU|WI)$`

**Rule:** Use `course_run_id` in filenames for course-term scoped artifacts (most files).  
**Rule:** Use `course_id` alone only when term does not matter (rare).

---

## NAMING PRINCIPLES

1. Deterministic: IDs derived consistently from available data (no randomness)
2. Stable: IDs change only if the underlying entity changes
3. Human-readable where possible
4. Machine-parseable via regex validation
5. Collision-resistant within entity type
6. No personal names in IDs (except student first name "Josh" if needed)

---

## FILE NAMING CONVENTIONS

### Global rule (applies to ALL course-controlled files)
Every file created/managed by this system MUST start with `{course_id}`.

**Validation:**
- ✓ filename begins with `MKTG6051...` or `MGMT6022...`
- ✗ filename begins with `CARLSON...` or `2026...` or `SPRING...`

---

### Universal File Naming Format (Module Content)

**Format:** `{CourseID}_M{ModuleNumber}.{TypeCode}_{short-description}.{extension}`

**Components:**
- **CourseID:** The course identifier, e.g., `MKTG6051`, `MGMT6022`
- **Module number:** Two digits prefixed by `M` (e.g., `M01`, `M02`, `M10`). Use `GK` for course-level materials (Grounded Knowledge).
- **Type codes:**
  - `.A` = Assignment
  - `.L` = Lecture
  - `.R` = Resource (article, book, video transcript, etc.)
  - `.B` = Business case
- **Short description:** Lowercase, hyphen-separated, no spaces or special characters
- **Extension:** Standard file extension (`.md`, `.pdf`, `.pptx`, `.docx`, `.xlsx`, `.csv`, `.txt`)

**Regex (module content):**
`^[A-Z]{2,10}[0-9]{3,5}_(M[0-9]{2}|GK)\.[ALRB]_[a-z0-9\-]+\.[a-z]+$`

**Examples (valid):**
- `MKTG6051_M01.A_chapter-12-questions.md`
- `MKTG6051_M02.L_survey-design.pptx`
- `MKTG6051_M02.R_demand-and-supply.pdf`
- `MKTG6051_M02.B_airbus-v-boeing.docx`
- `MKTG6051_GK_syllabus.pdf`
- `MGMT6022_M03.A_competitive-analysis.md`
- `MGMT6022_M05.L_corporate-strategy.pptx`
- `MGMT6022_M05.R_porter-five-forces.pdf`

**Note:** The course ID MUST prefix every file. Files with `GK` (Grounded Knowledge) are course-wide materials like syllabus and schedule that are not module-specific.

---

### Grounded Knowledge Files (GK)

**Pattern:** `{course_id}_GK_{doc-type}.md`

**Allowed doc-type values:**
- `course-core`
- `course-schedule`
- `student-profile`

**Regex:**
`^[A-Z]{2,10}[0-9]{3,5}_GK_(course-core|course-schedule|student-profile)\.md$`

**Examples (valid):**
- `MGMT6022_GK_course-core.md`
- `MGMT6022_GK_course-schedule.md`
- `MGMT6022_GK_student-profile.md`
- `MKTG6051_GK_course-core.md`

**Examples (invalid):**
- `CARLSON-SCHOOL_GK_course-core.md` (not a course id)
- `MGMT6022-2026-SP_GK_course-core.md` (term_id should not be in filename)
- `MGMT6022_GK_course_core.md` (use hyphens, not underscores in doc-type)

---

### INDEX File

**Pattern:** `{course_id}_GK_index.json`

**Regex:**
`^[A-Z]{2,10}[0-9]{3,5}_GK_index\.json$`

**Example:**
- `MGMT6022_GK_index.json`
- `MKTG6051_GK_index.json`

---

### Module Package (Folder)

**Module folder MUST start with `{course_id}` and include `{module_id}`.**

**Pattern:** `{course_id}_M{NN}/`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}/$`

**Examples:**
- `MKTG6051_M01/`
- `MKTG6051_M10/`
- `MGMT6022_M03/`

---

### Module Package (ZIP)

**Pattern:** `{course_id}_M{NN}.zip`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.zip$`

**Examples:**
- `MKTG6051_M01.zip`
- `MKTG6051_M10.zip`
- `MGMT6022_M03.zip`

---

### Module Manifest (Inside Module Package)

**Pattern:** `{course_id}_M{NN}.manifest.md`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.manifest\.md$`

**Examples:**
- `MKTG6051_M01.manifest.md`
- `MKTG6051_M03.manifest.md`
- `MGMT6022_M05.manifest.md`

**Validation rules:**
- ✓ module_id in manifest MUST match the parent module folder/zip module_id
- ✓ filename MUST start with course_id

---
---

### Curated Module File (Optional)

**Pattern:** `{course_id}_M{NN}_curated.md`

**Regex:**
`^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}_curated\.md$`

**Examples:**
- `MGMT6022_M03_curated.md`
- `MKTG6051_M05_curated.md`

---

### Module Content Files (Using Type Codes)

All module content files use the universal format with type codes.

**Pattern:** `{CourseID}_M{NN}.{TypeCode}_{short-description}.{extension}`

**Type Codes:**
- `.A` = Assignment (instructions, rubric, template, submission)
- `.L` = Lecture (slides, notes, video transcripts)
- `.R` = Resource (articles, books, video transcripts, references)
- `.B` = Business case

**Examples (Assignments):**
- `MKTG6051_M01.A_chapter-12-questions.md`
- `MKTG6051_M02.A_survey-design-rubric.pdf`
- `MGMT6022_M03.A_competitive-analysis-instructions.pdf`

**Examples (Lectures):**
- `MKTG6051_M02.L_survey-design.pptx`
- `MGMT6022_M05.L_corporate-strategy-slides.pptx`
- `MKTG6051_M03.L_market-research-notes.md`

**Examples (Resources):**
- `MKTG6051_M02.R_demand-and-supply.pdf`
- `MGMT6022_M05.R_porter-five-forces.pdf`
- `MKTG6051_M01.R_marketing-basics-article.pdf`

**Examples (Business Cases):**
- `MKTG6051_M02.B_airbus-v-boeing.docx`
- `MGMT6022_M04.B_apple-supply-chain.pdf`

**Regex (module content):**
`^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.[ALRB]_[a-z0-9\-]+\.[a-z]+$`

---

### Course-Level Files (GK - Grounded Knowledge)

For course-wide materials not tied to a specific module (syllabus, schedule documents, etc.), use `GK` instead of module number.

**Pattern:** `{CourseID}_GK_{short-description}.{extension}`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_GK_[a-z0-9\-]+\.[a-z]+$`

**Examples:**
- `MKTG6051_GK_syllabus.pdf`
- `MKTG6051_GK_schedule.pdf`
- `MGMT6022_GK_course-policies.pdf`

---

### Ad-Hoc Uploaded Files (User-provided, not system-controlled)

User-provided uploads may keep their original names.

**However:** Once a user-provided file is curated into system-managed storage, it MUST be renamed to conform to the standards above (starts with course_id).

---

### Agent Instructions File (One Per Course)

**Purpose:** Each course requires its own dedicated Agent Instructions file. This enforces the **one-course-per-agent** model. A single agent should only manage one course.

**Pattern:** `{course_id}_Agent_Instructions.md`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_Agent_Instructions\.md$`

**Examples:**
- `MKTG6051_Agent_Instructions.md`
- `MABA6321_Agent_Instructions.md`
- `MGMT6305_Agent_Instructions.md`
- `MGMT6465_Agent_Instructions.md`

**Location:** Inside the course folder at `course_final_build/{course_id}/`

**Usage:** Paste into Custom GPT instructions field (not uploaded as file). Each Custom GPT agent should be configured with exactly one course's Agent Instructions.

**Important:** Do NOT create multi-course agent instructions. The system is designed for **one course per agent** to ensure accuracy and prevent information mixing across courses.

---

## ENTITY ID STANDARDS

### Module ID (`module_id`)
**Format:** `M{NN}` where NN is two-digit zero-padded number, or `GK` for course-level materials.

**Examples:** `M01`, `M02`, `M10`, `GK`  
**Regex:** `^(M[0-9]{2}|GK)$`

**Derivation:**
1. If syllabus provides module numbers, normalize to 2 digits.
2. If "Week 1", map to `M01`, etc.
3. If no structure, assign sequentially based on schedule order.
4. Module IDs do not change mid-term.

---

### Assignment ID (`assignment_id`)
**Supported formats:**
- Generic numbered: `A{NN}` e.g. `A01`
- Typed numbered: `{TYPE}-{NN}` e.g. `QUIZ-01`
- Named: `{TYPE}-{NAME}` e.g. `EXAM-MIDTERM`, `PROJ-FINAL`
- Hashed disambiguation: `{TYPE}-{NN}-{HASH4}` e.g. `ESSAY-02-A7F3`

**Regex (union, practical):**
`^(A[0-9]{2}|[A-Z]+-[0-9]{2}|[A-Z]+-[A-Z0-9\-]+|[A-Z]+-[0-9]{2}-[A-F0-9]{4})$`

**Hash rule (only when needed):**
```

hash_input = f"{assignment_title}_{due_date_iso}"
hash_suffix = sha256(hash_input)[:4].upper()
assignment_id = f"{type_code}-{seq_num:02d}-{hash_suffix}"

```

---

### Exam ID
Exams are assignments, so use `assignment_id` forms:
- `EXAM-MIDTERM`
- `EXAM-FINAL`
- `EXAM-01`

---

### Reading ID
**Format:** `R{NN}` or `M{NN}-R{NN}`  
**Regex:** `^(M[0-9]{2}-)?R[0-9]{2}$`

---

### Discussion ID
**Format:** `D{NN}` or `M{NN}-D{NN}`  
**Regex:** `^(M[0-9]{2}-)?D[0-9]{2}$`

---

## METADATA FIELD STANDARDS (GK FILES)

Required fields:
- `course_id`: e.g. `MGMT6022`
- `term_id`: e.g. `2026-SP`
- `course_run_id`: e.g. `MGMT6022-2026-SP`
- `doc_type`: one of `course_core`, `course_schedule`, `student_profile`, `index`, `module_manifest`, `curated_module`
- `last_updated`: `YYYY-MM-DD`
- `timezone`: IANA tz, prefer `America/Chicago`

---

## CROSS-REFERENCE FORMAT

**Format:** `{filename}#{section_id}` or `{filename}#{section_id}({entity_id})`

**Rule:** When referencing course-scoped files, filenames use `{course_id}_GK_` prefix.

**Examples:**
- `MGMT6022_GK_course-core.md#grading-policy`
- `MGMT6022_GK_course-schedule.md#assignment-calendar(A03)`
- `MKTG6051_M03/MKTG6051_M03.manifest.md#metadata`
- `MKTG6051_M02.A_survey-design-instructions.pdf`

---

## VALIDATION REGEX SUMMARY

| Item | Regex |
|---|---|
| course_id | `^[A-Z]{2,10}[0-9]{3,5}$` |
| term_id | `^(20[0-9]{2})-(FA\|SP\|SU\|WI)$` |
| course_run_id | `^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA\|SP\|SU\|WI)$` |
| module_id | `^(M[0-9]{2}\|GK)$` |
| GK filename | `^[A-Z]{2,10}[0-9]{3,5}_GK_(course-core\|course-schedule\|student-profile)\.md$` |
| index filename | `^[A-Z]{2,10}[0-9]{3,5}_GK_index\.json$` |
| agent instructions | `^[A-Z]{2,10}[0-9]{3,5}_Agent_Instructions\.md$` |
| module folder | `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}/$` |
| module zip | `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.zip$` |
| module manifest | `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.manifest\.md$` |
| module content file | `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.[ALRB]_[a-z0-9\-]+\.[a-z]+$` |
| course-level GK file | `^[A-Z]{2,10}[0-9]{3,5}_GK_[a-z0-9\-]+\.[a-z]+$` |

---

## EXAMPLES: COMPLETE FILE AND ENTITY SET

**Course:** MKTG6051  
**Term:** Spring 2026

### Required identifiers
- `course_id`: `MKTG6051`
- `term_id`: `2026-SP`
- `course_run_id`: `MKTG6051-2026-SP`

### GK files (Grounded Knowledge)
- `MKTG6051_GK_course-core.md`
- `MKTG6051_GK_course-schedule.md`
- `MKTG6051_GK_student-profile.md`
- `MKTG6051_GK_index.json`

### Agent Instructions (One Per Course)
- `MKTG6051_Agent_Instructions.md`

### Course-Level Materials (GK)
- `MKTG6051_GK_syllabus.pdf`
- `MKTG6051_GK_schedule.pdf`

### Modules
- Folder: `MKTG6051_M01/`
- ZIP: `MKTG6051_M01.zip`
- Manifest: `MKTG6051_M01.manifest.md`

### Module Content Files (by Type Code)

**Assignments (.A):**
- `MKTG6051_M01.A_chapter-12-questions.md`
- `MKTG6051_M02.A_survey-design-rubric.pdf`
- `MKTG6051_M03.A_market-analysis-instructions.pdf`

**Lectures (.L):**
- `MKTG6051_M02.L_survey-design.pptx`
- `MKTG6051_M03.L_market-research-slides.pptx`
- `MKTG6051_M05.L_pricing-strategy-notes.md`

**Resources (.R):**
- `MKTG6051_M02.R_demand-and-supply.pdf`
- `MKTG6051_M04.R_consumer-behavior-article.pdf`
- `MKTG6051_M01.R_marketing-basics.pdf`

**Business Cases (.B):**
- `MKTG6051_M02.B_airbus-v-boeing.docx`
- `MKTG6051_M04.B_tesla-marketing-strategy.pdf`

---

**END OF DOCUMENT**
