# Course Assistant Builder

**Official builder repository for creating AI Course Assistant agents**

This repository contains the complete system for building custom GPT-based course assistants. It includes templates, schemas, validation tools, and operational protocols for creating structured knowledge files that enable AI agents to provide accurate, contextual support for college courses.

---

## 🎯 What This System Does

The Course Assistant Builder helps you create AI agents that can:

- Answer questions about course policies, grading, and structure
- Provide accurate due dates and deadlines
- Help students plan assignments and manage coursework
- Reference course materials with proper citations
- Support module-based learning content

Each agent is **single-course, single-term, single-student** focused for maximum accuracy and relevance.

---

## 📋 Quick Start

### Building a Course Assistant (5 Steps)

1. **Create Required Files** (using templates/)
   - `{course_run_id}.course-core.md` - Policies, grading, structure
   - `{course_run_id}.course-schedule.md` - Dates, deadlines, assignments
   - `{course_run_id}.student-profile.md` - Student context and writing style

2. **Generate INDEX** (using validation script)
   ```bash
   python validation/validate_system.py --generate-index
   ```

3. **Validate Files** (using validation script)
   ```bash
   python validation/validate_system.py --validate-all
   ```

4. **Configure Agent** (using protocols/)
   - Customize `protocols/41_Agent_Instructions_Revised.md` for your course
   - Upload the 3 knowledge files + INDEX.json to custom GPT

5. **Verify Setup** (using setup/)
   - Follow prompts in `setup/50_Setup_Prompt_Sequence.md`
   - Run tests from `setup/51_Acceptance_Test_Suite.md`

---

## 📁 Repository Structure

```
course-assistant-build-2/
│
├── README.md                    # This file
├── REPOSITORY_ANALYSIS.md       # Detailed file inventory and analysis
│
├── grounded/                    # Core documentation and standards
│   ├── 03_Final_File_Set_Register.md         # Authoritative file specifications
│   ├── 04_Authority_and_Precedence_Rules.md  # Conflict resolution rules
│   ├── 05_Naming_and_ID_Standard.md          # Naming conventions and patterns
│   ├── 06_Index_and_Manifest_System.md       # INDEX system documentation
│   └── 07_Date_Time_Standard.md              # Date/time formatting rules
│
├── templates/                   # File creation templates
│   ├── 20_Course_Core_Template.md            # Template for course-core.md
│   ├── 21_Course_Schedule_Template.md        # Template for course-schedule.md
│   ├── 22_Student_Profile_Template.md        # Template for student-profile.md
│   ├── 23_Index_Manifest_Template.yaml       # Template for INDEX.json
│   └── 24_Module_Package_Template.md         # Template for module manifests
│
├── schema/                      # JSON schemas for validation
│   ├── schema.course_core.json               # Validates course-core.md
│   ├── schema.course_schedule.json           # Validates course-schedule.md
│   ├── schema.student_profile.json           # Validates student-profile.md
│   ├── schema.index_manifest.json            # Validates INDEX.json
│   ├── schema.module_package.json            # Validates module manifests
│   └── schema.group_project.json             # Validates group project sections
│
├── protocols/                   # Operational protocols
│   ├── 30_Module_Upload_and_Usage_Protocol.md    # How to upload modules
│   ├── 40_Retrieval_Protocol.md                  # How agents retrieve info
│   └── 41_Agent_Instructions_Revised.md          # Agent instruction template
│
├── setup/                       # Setup and testing
│   ├── 50_Setup_Prompt_Sequence.md           # Verification prompts
│   └── 51_Acceptance_Test_Suite.md           # Comprehensive tests
│
└── validation/                  # Validation tools
    └── validate_system.py                    # Validation script
```

---

## 🎓 Core Concepts

### The 4-File System

Every course assistant requires exactly 4 files:

1. **Course Core** (`course-core.md`) - Tier 1 Authority (HIGHEST)
   - Complete course syllabus content
   - Course policies, grading structure, instructor info
   - Group project definition
   - Authoritative for all course requirements

2. **Course Schedule** (`course-schedule.md`) - Tier 2 Authority  
   - ALL dates, deadlines, due times
   - Module sequence and timeline
   - Authoritative for temporal information

3. **Student Profile** (`student-profile.md`) - Tier 3 Authority
   - Student identification (first name only)
   - Comprehensive writing style profile
   - Timezone and preferences

4. **INDEX** (`index.json`) - Tier 4 Authority
   - Machine-parseable index for retrieval
   - Links all entities (modules, assignments, etc.)
   - Enables verification and completeness checks

### Authority Hierarchy (6 Tiers)

When information conflicts, priority order:

1. **Tier 1:** Course Core (syllabus, policies, structure)
2. **Tier 2:** Course Schedule (dates/deadlines)
3. **Tier 3:** Student Profile (student context)
4. **Tier 4:** INDEX (retrieval metadata)
5. **Tier 5:** Module Working Memory Files
6. **Tier 6:** Ad-Hoc Uploads

See `grounded/04_Authority_and_Precedence_Rules.md` for complete rules.

### Naming Convention

All system files use strict naming patterns:

- **course_id:** Course code only (e.g., `MGMT6022`)
- **term_id:** Year and term (e.g., `2026-SP`) - used in metadata only
- **GK files:** Use `{course_id}_GK_` prefix (e.g., `MGMT6022_GK_course-core.md`)

Example filenames:
- `MGMT6022_GK_course-core.md`
- `MGMT6022_GK_course-schedule.md`
- `MGMT6022_GK_student-profile.md`
- `MGMT6022_GK_index.json`

See `grounded/05_Naming_and_ID_Standard.md` for complete patterns.

---

## 🛠️ Using the Validation Script

The validation script (`validation/validate_system.py`) provides:

### Validate All Files
```bash
python validation/validate_system.py --validate-all
```

### Validate Specific File
```bash
python validation/validate_system.py --validate-file path/to/file.md
```

### Generate INDEX
```bash
python validation/validate_system.py --generate-index --course-id MGMT6022-2026-SP
```

### Check Naming Conventions
```bash
python validation/validate_system.py --check-naming path/to/files/
```

See validation script for complete options and usage.

---

## 📖 Key Documentation Files

Start with these files to understand the system:

1. **File Specifications**
   - `grounded/03_Final_File_Set_Register.md` - What each file type contains

2. **Standards and Rules**
   - `grounded/04_Authority_and_Precedence_Rules.md` - Conflict resolution
   - `grounded/05_Naming_and_ID_Standard.md` - Naming patterns
   - `grounded/07_Date_Time_Standard.md` - Date/time formatting

3. **Operational Protocols**
   - `protocols/40_Retrieval_Protocol.md` - How agents retrieve information
   - `protocols/30_Module_Upload_and_Usage_Protocol.md` - Module workflow

4. **Setup and Testing**
   - `setup/50_Setup_Prompt_Sequence.md` - Verification steps
   - `setup/51_Acceptance_Test_Suite.md` - Quality assurance tests

---

## 🎯 Design Principles

This system is built on these core principles:

1. **Single Source of Truth**
   - Each fact appears in exactly one authoritative location
   - Conflicts are resolved by authority hierarchy

2. **Structured Over Prose**
   - Use tables, lists, and sections with anchors
   - Enable precise retrieval targeting

3. **Explicit Over Implicit**
   - Mark unknowns as "TBD" rather than guessing
   - Include metadata for all entities

4. **Privacy By Default**
   - Anonymize group member names (Member 01, Member 02, etc.)
   - Include only operationally necessary information

5. **Validation First**
   - All files validated against JSON schemas
   - Automated checks for completeness and correctness

---

## 🔧 Requirements

- **Python 3.7+** (for validation script)
- **JSON Schema validator** (install via `pip install jsonschema`)
- **Custom GPT** or compatible AI platform
- Course materials (syllabus, schedule, etc.)

---

## 📝 Example Workflow

Here's a complete example of building a course assistant:

### Step 1: Gather Course Materials
- Download syllabus PDF
- Export schedule to spreadsheet
- Collect student writing samples

### Step 2: Create Files from Templates
```bash
# Copy templates
cp templates/20_Course_Core_Template.md MGMT6022_GK_course-core.md
cp templates/21_Course_Schedule_Template.md MGMT6022_GK_course-schedule.md
cp templates/22_Student_Profile_Template.md MGMT6022_GK_student-profile.md

# Fill in content following template structure
```

### Step 3: Validate and Generate INDEX
```bash
# Validate each file
python validation/validate_system.py --validate-file MGMT6022_GK_course-core.md
python validation/validate_system.py --validate-file MGMT6022_GK_course-schedule.md
python validation/validate_system.py --validate-file MGMT6022_GK_student-profile.md

# Generate INDEX
python validation/validate_system.py --generate-index --course-id MGMT6022-2026-SP
```

### Step 4: Configure Custom GPT
1. Create new Custom GPT in ChatGPT
2. Customize `protocols/41_Agent_Instructions_Revised.md` with course details
3. Paste instructions into GPT configuration
4. Upload 4 files: course-core.md, course-schedule.md, student-profile.md, index.json

### Step 5: Verify and Test
1. Follow `setup/50_Setup_Prompt_Sequence.md` (7 verification prompts)
2. Run tests from `setup/51_Acceptance_Test_Suite.md`
3. Fix any issues and re-test

### Step 6: Operational Use
- Student uploads module content as needed
- Agent references knowledge files with proper citations
- Update files when course changes (validate changes)

---

## 🤝 Contributing

This is the official builder repository. Changes should:

1. Maintain backward compatibility with existing builds
2. Follow established naming conventions
3. Include schema updates if file structures change
4. Update relevant documentation
5. Pass all validation tests

---

## 📄 License

This is a private repository for course assistant development.

---

## 🆘 Support

For questions or issues:

1. Review `REPOSITORY_ANALYSIS.md` for detailed file purposes
2. Check relevant documentation in `grounded/` directory
3. Consult protocol files in `protocols/` directory
4. Run validation script to diagnose structural issues

---

## 📊 System Status

- **Current Version:** 1.0
- **File Types:** 4 required + module packages
- **Authority Tiers:** 6-tier hierarchy
- **Validation:** Automated via JSON schemas
- **Testing:** 7-step setup + comprehensive test suite

---

**Last Updated:** 2026-02-05  
**Repository:** dweebzxx/course-assistant-build-2
