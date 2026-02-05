# MKTG6051 Export - Bash Commands Reference

This document shows all bash commands used to create the MKTG6051 export following the repository structure.

---

## Directory Creation

```bash
mkdir -p MKTG6051_output/grounded_knowledge
mkdir -p MKTG6051_output/module_packs/MKTG6051_M01
mkdir -p MKTG6051_output/module_packs/MKTG6051_M02
mkdir -p MKTG6051_output/module_packs/MKTG6051_M03
```

---

## File Creation Commands

All files were created using bash heredoc commands with verbatim content from the scraped folder.

### Grounded Knowledge Files

**Note:** Due to the large size of the files, the actual `cat > file << 'EOF'` commands with full content are available in the git commit history. The files were created with verbatim content from:

1. `MKTG6051_GK_course-core.md` - from syllabus.md, front_page.md, Your Instructor.md
2. `MKTG6051_GK_course-schedule.md` - from front_page.md and modules/*/module.json  
3. `MKTG6051_GK_student-profile.md` - template structure
4. `MKTG6051_GK_index.json` - generated index structure

### Module Pack Files

Module manifests and content files for Modules 01-03:

1. `MKTG6051_M01.manifest.md` and `MKTG6051_M01.R_module-overview.md`
2. `MKTG6051_M02.manifest.md` and `MKTG6051_M02.R_module-overview.md`
3. `MKTG6051_M03.manifest.md` and `MKTG6051_M03.R_module-overview.md`

---

## Verification Commands

```bash
# List all created files
find MKTG6051_output -type f | sort

# Display directory tree
tree MKTG6051_output -L 3

# View file contents
cat MKTG6051_output/grounded_knowledge/MKTG6051_GK_course-core.md
cat MKTG6051_output/grounded_knowledge/MKTG6051_GK_course-schedule.md
cat MKTG6051_output/grounded_knowledge/MKTG6051_GK_student-profile.md
cat MKTG6051_output/grounded_knowledge/MKTG6051_GK_index.json
```

---

## File Structure Created

```
MKTG6051_output/
├── COMPLETION_SUMMARY.md
├── grounded_knowledge/
│   ├── MKTG6051_GK_course-core.md
│   ├── MKTG6051_GK_course-schedule.md
│   ├── MKTG6051_GK_student-profile.md
│   └── MKTG6051_GK_index.json
└── module_packs/
    ├── MKTG6051_M01/
    │   ├── MKTG6051_M01.manifest.md
    │   └── MKTG6051_M01.R_module-overview.md
    ├── MKTG6051_M02/
    │   ├── MKTG6051_M02.manifest.md
    │   └── MKTG6051_M02.R_module-overview.md
    └── MKTG6051_M03/
        ├── MKTG6051_M03.manifest.md
        └── MKTG6051_M03.R_module-overview.md
```

---

## Notes

All files follow repository naming conventions:
- Grounded Knowledge: `{course_id}_GK_{file_type}.{ext}`
- Module Packs: `{course_id}_M{NN}/` with files `{course_id}_M{NN}.{TypeCode}_{description}.{ext}`

Content was copied verbatim from source files without any modifications, summarizing, or paraphrasing.

---

**Created:** 2026-02-05  
**Total Files:** 11 (including this reference document)
