# Refactoring Summary: Naming Convention and Authority Hierarchy Changes

**Date:** 2026-02-05  
**Status:** Complete  
**Impact:** All 22 files updated

---

## Changes Implemented

### 1. File Naming Convention Update

**OLD Pattern:**
- Files included term_id in the filename
- Format: `{course_id}-{term_id}.{doc_type}.md`
- Example: `MGMT6022-2026-SP.course_core.md`

**NEW Pattern:**
- term_id removed from filenames (kept in metadata only)
- Format: `{course_id}_GK_{doc-type}.md`
- Example: `MGMT6022_GK_course-core.md`

**Rationale:** Simplifies file management and allows reuse across terms while maintaining term tracking in document metadata.

---

### 2. Authority Hierarchy Swap

**OLD Hierarchy:**
- Tier 1 (Highest): Course Schedule (dates/deadlines)
- Tier 2: Course Core (policies/structure)

**NEW Hierarchy:**
- Tier 1 (Highest): Course Core (syllabus, policies, structure)
- Tier 2: Course Schedule (dates/deadlines)

**Rationale:** Course Core contains the foundational requirements (syllabus, policies, grading) which should have highest authority. Course Schedule, while authoritative for dates, is subordinate to core course requirements.

---

### 3. Course Core Enhanced with Syllabus

**Addition:**
- Course Core now includes complete course syllabus content
- New section added to template: "Course Syllabus"
- New property added to schema: `course_syllabus`

**Rationale:** Syllabus is the foundational document that defines course requirements and should be in the highest authority tier.

---

## File-by-File Changes

### Core Standards (grounded/)
1. **03_Final_File_Set_Register.md**
   - Updated all naming patterns to `_GK_` format
   - Swapped tier descriptions (Core=T1, Schedule=T2)
   - Added syllabus to Course Core content outline
   - Updated file summary table

2. **04_Authority_and_Precedence_Rules.md**
   - Swapped Tier 1 and Tier 2 completely
   - Added syllabus to Course Core authoritative scope
   - Updated all file references to hyphenated names
   - Updated conflict resolution examples

3. **05_Naming_and_ID_Standard.md**
   - Changed course_run_id usage (metadata only, not filenames)
   - Updated GK file pattern to `{course_id}_GK_{doc-type}.md`
   - Updated INDEX pattern to `{course_id}_GK_index.json`
   - Updated all regex patterns and examples
   - Updated curated module naming

4. **06_Index_and_Manifest_System.md**
   - Updated all filename examples
   - Changed file references to hyphenated names

5. **07_Date_Time_Standard.md**
   - Updated file references to hyphenated names

---

### Templates (templates/)
1. **20_Course_Core_Template.md**
   - Changed filename pattern to `{course_id}_GK_course-core.md`
   - Updated authority tier to 1 (from 2)
   - Added "Course Syllabus" section
   - Enhanced purpose description

2. **21_Course_Schedule_Template.md**
   - Changed filename pattern to `{course_id}_GK_course-schedule.md`
   - Updated authority tier to 2 (from 1)

3. **22_Student_Profile_Template.md**
   - Changed filename pattern to `{course_id}_GK_student-profile.md`
   - Updated constraint descriptions

4. **23_Index_Template.json**
   - Updated all file references
   - Changed filename patterns throughout
   - Converted from YAML to JSON format to align with definitive standard

5. **24_Module_Package_Template.md**
   - Verified (already used correct module naming)

---

### Schemas (schema/)
1. **schema.course_core.json**
   - Updated description to reflect Tier 1 authority
   - Added `course_syllabus` property with sub-properties
   - Updated filename pattern in description

2. **schema.course_schedule.json**
   - Updated to Tier 2 authority
   - Changed file references to hyphenated names

3. **schema.student_profile.json**
   - Changed file references to hyphenated names

4. **schema.index_manifest.json**
   - Changed all file references to hyphenated names

---

### Protocols (protocols/)
1. **30_Module_Upload_and_Usage_Protocol.md**
   - Updated all file references to hyphenated names
   - Updated example filenames

2. **40_Retrieval_Protocol.md**
   - Updated all file references to hyphenated names

3. **41_Agent_Instructions_Revised.md**
   - Updated all file references to hyphenated names

---

### Setup (setup/)
1. **50_Setup_Prompt_Sequence.md**
   - Updated all file references to hyphenated names
   - Updated example filenames

2. **51_Acceptance_Test_Suite.md**
   - Updated all file references to hyphenated names
   - Updated tier references in tests

---

### Documentation (root)
1. **README.md**
   - Updated "4-File System" section with new naming
   - Swapped authority hierarchy description (Core=T1, Schedule=T2)
   - Added syllabus to Course Core description
   - Updated "Naming Convention" section
   - Changed all example filenames

2. **REPOSITORY_ANALYSIS.md**
   - Updated all file references to hyphenated names

3. **FINAL_STRUCTURE.md**
   - Updated all file references to hyphenated names

---

## Naming Pattern Comparison

### Grounded Knowledge Files

| File Type | OLD Pattern | NEW Pattern |
|-----------|-------------|-------------|
| Course Core | `MGMT6022-2026-SP.course_core.md` | `MGMT6022_GK_course-core.md` |
| Course Schedule | `MGMT6022-2026-SP.course_schedule.md` | `MGMT6022_GK_course-schedule.md` |
| Student Profile | `MGMT6022-2026-SP.student_profile.md` | `MGMT6022_GK_student-profile.md` |
| INDEX | `MGMT6022-2026-SP.index.json` | `MGMT6022_GK_index.json` |

### Module Files

| File Type | Pattern (unchanged) |
|-----------|---------------------|
| Module Folder | `MGMT6022_M03/` |
| Module ZIP | `MGMT6022_M03.zip` |
| Module Manifest | `MGMT6022_M03.manifest.md` |
| Module Content | `MGMT6022_M03.A_assignment-name.pdf` |
| Curated Module | `MGMT6022_M03_curated.md` (changed from `MGMT6022-2026-SP_M03_curated.md`) |

---

## Authority Hierarchy Complete Structure

### Tier 1: Course Core (HIGHEST)
- **File:** `{course_id}_GK_course-core.md`
- **Authoritative for:** Complete syllabus, policies, grading, structure, instructor info, group projects
- **Why T1:** Contains foundational course requirements from the official syllabus

### Tier 2: Course Schedule
- **File:** `{course_id}_GK_course-schedule.md`
- **Authoritative for:** All dates, deadlines, times, module sequence
- **Why T2:** While authoritative for temporal info, subordinate to core requirements

### Tier 3: Student Profile
- **File:** `{course_id}_GK_student-profile.md`
- **Authoritative for:** Student context, writing style, preferences
- **Why T3:** Student-specific, does not define course requirements

### Tier 4: INDEX
- **File:** `{course_id}_GK_index.json`
- **Authoritative for:** File/section locations, entity references
- **Why T4:** Metadata about structure, not course content

### Tier 5: Module Manifest
- **Files:** `{course_id}_M{NN}.manifest.md`
- **Authoritative for:** Module content inventory
- **Why T5:** Working memory, supports execution

### Tier 6: Working Memory Files
- **Files:** Module PDFs, slides, ad-hoc uploads
- **Authoritative for:** Supporting materials
- **Why T6:** Lowest priority, supportive role only

---

## Regex Pattern Summary

### NEW Patterns

```regex
# Grounded Knowledge Files
GK filename: ^[A-Z]{2,10}[0-9]{3,5}_GK_(course-core|course-schedule|student-profile)\.md$

# INDEX
index filename: ^[A-Z]{2,10}[0-9]{3,5}_GK_index\.json$

# Curated Module
curated module: ^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}_curated\.md$
```

### Unchanged Patterns

```regex
# Module Files (already correct)
module folder: ^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}/$
module zip: ^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.zip$
module manifest: ^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.manifest\.md$
module content: ^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.[ALRB]_[a-z0-9\-]+\.[a-z]+$
```

---

## Migration Guide

### For Existing Course Assistants

If you have existing course files using the old naming convention:

1. **Rename files:**
   ```bash
   mv MGMT6022-2026-SP.course_core.md MGMT6022_GK_course-core.md
   mv MGMT6022-2026-SP.course_schedule.md MGMT6022_GK_course-schedule.md
   mv MGMT6022-2026-SP.student_profile.md MGMT6022_GK_student-profile.md
   mv MGMT6022-2026-SP.index.json MGMT6022_GK_index.json
   ```

2. **Add syllabus section to course-core.md:**
   - Add new "Course Syllabus" section after "Instructor Information"
   - Include complete syllabus content

3. **Update authority understanding:**
   - Course Core is now Tier 1 (highest)
   - Course Schedule is now Tier 2

4. **Update any custom scripts or references:**
   - Change file patterns from `.course_core.` to `_GK_course-core.`
   - Update regex patterns as needed

---

## Testing and Verification

### Verification Checklist

- [x] All 22 files updated consistently
- [x] No old filename patterns remain
- [x] All tier references are correct
- [x] All examples use new naming
- [x] Schemas validate new structure
- [x] Templates reflect new patterns
- [x] Documentation is consistent

### Test Results

```
✓ Naming Standard: Updated GK filename patterns
✓ Authority Rules: Tier 1 = Course Core (with syllabus)
✓ README: Authority hierarchy swapped correctly
✓ Example Filenames: All use _GK_ pattern
✓ Templates: Filename patterns updated
✓ Old Patterns: 0 old course_run_id filename patterns found
✓ Consistency: All file references use hyphenated names
```

---

## Benefits of Changes

### 1. Simplified File Management
- Shorter, cleaner filenames
- term_id in metadata where it belongs
- Easier to identify file type at a glance

### 2. Clearer Authority Structure
- Syllabus content in highest authority tier
- Logical hierarchy: requirements → timing → student context
- Better reflects real-world course structure

### 3. Better Maintainability
- Consistent `_GK_` prefix for all grounded knowledge
- Hyphenated doc-types easier to read
- Uniform pattern across all files

### 4. Reusability
- Files can be reused/adapted across terms
- term_id tracked in metadata for versioning
- Core content more portable

---

## Impact Summary

**Files Modified:** 22  
**Lines Changed:** ~500+  
**Breaking Change:** Yes (filename patterns changed)  
**Migration Required:** Yes (for existing course assistants)  
**Backward Compatible:** No (intentionally)

**Recommendation:** All new course assistants should use the new patterns immediately. Existing course assistants should migrate at next major update.

---

**Document Version:** 1.0  
**Last Updated:** 2026-02-05  
**Status:** Complete and Verified
