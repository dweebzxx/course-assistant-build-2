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
- ✓ filename begins with `MGMT6022...`
- ✗ filename begins with `CARLSON...` or `2026...` or `SPRING...`

---

### Grounded Knowledge Files (GK)

**Pattern:** `{course_run_id}.{doc_type}.md`

**Allowed doc_type values:**
- `course_core`
- `course_schedule`
- `student_profile`

**Regex:**
`^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA|SP|SU|WI)\.(course_core|course_schedule|student_profile)\.md$`

**Examples (valid):**
- `MGMT6022-2026-SP.course_core.md`
- `MGMT6022-2026-SP.course_schedule.md`
- `MGMT6022-2026-SP.student_profile.md`

**Examples (invalid):**
- `CARLSON-SCHOOL-2026-SP.course_core.md` (not a course id)
- `MGMT6022-2026-SP-SEC01.course_core.md` (section not part of this standard)
- `MGMT6022.course_core.md` (missing term scoping)

---

### INDEX File

**Pattern:** `{course_run_id}.index.json`

**Regex:**
`^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA|SP|SU|WI)\.index\.json$`

**Example:**
- `MGMT6022-2026-SP.index.json`

---

### Module Package (Folder)

**Module folder MUST start with `{course_id}` and include `{module_id}`.**

**Pattern:** `{course_id}.module_{module_id}/`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}\.module_M[0-9]{2}/$`

**Examples:を見る**
- `MGMT6022.module_M01/`
- `MGMT6022.module_M10/`

---

### Module Package (ZIP)

**Pattern:** `{course_id}.module_{module_id}.zip`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}\.module_M[0-9]{2}\.zip$`

**Examples:**
- `MGMT6022.module_M01.zip`
- `MGMT6022.module_M10.zip`

---

### Module Manifest (Inside Module Package)

**Pattern:** `{course_id}.module_{module_id}.module_manifest.md`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}\.module_M[0-9]{2}\.module_manifest\.md$`

**Examples:**
- `MGMT6022.module_M01.module_manifest.md`

**Validation rules:**
- ✓ module_id in manifest MUST match the parent module folder/zip module_id
- ✓ filename MUST start with course_id

---

### Curated Module File (Optional)

**Pattern:** `{course_run_id}.module_{module_id}_curated.md`

**Regex:**
`^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA|SP|SU|WI)\.module_M[0-9]{2}_curated\.md$`

**Example:**
- `MGMT6022-2026-SP.module_M03_curated.md`

---

### Assignment Files (Required course_id prefix)

All assignment artifacts MUST start with `{course_id}`.

**Pattern (general):**
`{course_run_id}.assignment_{assignment_id}.{artifact_type}.{ext}`

**Where:**
- `artifact_type` examples: `instructions`, `rubric`, `submission`, `notes`, `feedback`
- `ext` examples: `md`, `pdf`, `docx`

**Regex (common case):**
`^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA|SP|SU|WI)\.assignment_[A-Z0-9\-]+\.[a-z0-9_]+\.[A-Za-z0-9]+$`

**Examples:**
- `MGMT6022-2026-SP.assignment_A01.instructions.md`
- `MGMT6022-2026-SP.assignment_QUIZ-01.submission.docx`
- `MGMT6022-2026-SP.assignment_PROJ-FINAL.rubric.pdf`

---

### Ad-Hoc Uploaded Files (User-provided, not system-controlled)

User-provided uploads may keep their original names.

**However:** Once a user-provided file is curated into system-managed storage, it MUST be renamed to conform to the standards above (starts with course_id).

---

## ENTITY ID STANDARDS

### Module ID (`module_id`)
**Format:** `M{NN}` where NN is two-digit zero-padded number.

**Examples:** `M01`, `M02`, `M10`  
**Regex:** `^M[0-9]{2}$`

**Derivation:**
1. If syllabus provides module numbers, normalize to 2 digits.
2. If “Week 1”, map to `M01`, etc.
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

**Rule:** When referencing course-scoped files, the filename must include `course_run_id` and therefore starts with `course_id`.

**Examples:**
- `MGMT6022-2026-SP.course_core.md#grading-policy`
- `MGMT6022-2026-SP.course_schedule.md#assignment-calendar(A03)`
- `MGMT6022.module_M03/MGMT6022.module_M03.module_manifest.md#metadata`

---

## VALIDATION REGEX SUMMARY

| Item | Regex |
|---|---|
| course_id | `^[A-Z]{2,10}[0-9]{3,5}$` |
| term_id | `^(20[0-9]{2})-(FA\|SP\|SU\|WI)$` |
| course_run_id | `^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA\|SP\|SU\|WI)$` |
| module_id | `^M[0-9]{2}$` |
| GK filename | `^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA\|SP\|SU\|WI)\.(course_core\|course_schedule\|student_profile)\.md$` |
| index filename | `^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA\|SP\|SU\|WI)\.index\.json$` |
| module folder | `^[A-Z]{2,10}[0-9]{3,5}\.module_M[0-9]{2}/$` |
| module zip | `^[A-Z]{2,10}[0-9]{3,5}\.module_M[0-9]{2}\.zip$` |
| module manifest | `^[A-Z]{2,10}[0-9]{3,5}\.module_M[0-9]{2}\.module_manifest\.md$` |
| assignment file (general) | `^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA\|SP\|SU\|WI)\.assignment_[A-Z0-9\-]+\.[a-z0-9_]+\.[A-Za-z0-9]+$` |

---

## EXAMPLES: COMPLETE FILE AND ENTITY SET

**Course:** MGMT6022  
**Term:** Spring 2026

### Required identifiers
- `course_id`: `MGMT6022`
- `term_id`: `2026-SP`
- `course_run_id`: `MGMT6022-2026-SP`

### GK files
- `MGMT6022-2026-SP.course_core.md`
- `MGMT6022-2026-SP.course_schedule.md`
- `MGMT6022-2026-SP.student_profile.md`
- `MGMT6022-2026-SP.index.json`

### Modules
- Folder: `MGMT6022.module_M01/`
- ZIP: `MGMT6022.module_M01.zip`
- Manifest: `MGMT6022.module_M01.module_manifest.md`

### Assignments
- `MGMT6022-2026-SP.assignment_A01.instructions.md`
- `MGMT6022-2026-SP.assignment_QUIZ-01.submission.docx`
- `MGMT6022-2026-SP.assignment_PROJ-FINAL.rubric.pdf`

---

**END OF DOCUMENT**
