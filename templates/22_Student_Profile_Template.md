# Student Profile Template

**Template Number:** 22  
**Document Type:** Grounded Knowledge File Template  
**Phase:** 4  
**Date:** 2026-01-25  
**Status:** Definitive template for student_profile.md

**Filename Pattern:** `{course_id}.student_profile.md`  
**Regex:** `^[A-Z0-9\-]+\.student_profile\.md$`  
**Authority Tier:** 3 (Authoritative for student context and preferences)  
**Example Filename:** `MGMT-5001-SEC01-2026-SP.student_profile.md`

**Purpose:** Captures student-specific context, preferences, constraints, and group project information to personalize agent responses and support pacing recommendations.

**Constraint:** This file is authoritative for student context ONLY. It may NOT contradict course requirements defined in course_core.md or course_schedule.md.

---

## Metadata
<!-- anchor: #metadata -->

| Field | Value |
|-------|-------|
| **course_id** | `{COURSE_ID}` |
| **term_id** | `{YYYY}-{TT}` |
| **doc_type** | `student_profile` |
| **last_updated** | `{YYYY-MM-DD}` |
| **timezone** | `America/Chicago` |
| **student_name** | `Josh` |

**Change Log (optional):**
- {YYYY-MM-DD}: {Description of change}

---

## Student Identification
<!-- anchor: #student-identification -->

| Field | Value |
|-------|-------|
| **First Name** | Josh |
| **Preferred Name** | {Josh or preferred name} |
| **Program** | {e.g., MBA, MS Finance, Undergraduate Marketing} |
| **Year** | {e.g., First year, Second year, Senior} |
| **Expected Graduation** | {Term and year, e.g., Spring 2027} |

---

## Learning Preferences
<!-- anchor: #learning-preferences -->

{Josh's learning preferences to help personalize agent interactions and recommendations.}

| Preference | Selection |
|------------|-----------|
| **Communication Style** | {Professional / Casual / Encouraging / Direct} |
| **Study Environment** | {e.g., "Library / Coffee shop / Home office"} |
| **Note-Taking Method** | {e.g., "Outline method with bullet points / Digital notes / Paper notes"} |
| **Planning Approach** | {e.g., "Prefers to start 5-7 days before deadline / Early starter / Just-in-time"} |

---

## Time Constraints
<!-- anchor: #time-constraints -->

### Weekly Availability

{Josh's typical weekly schedule showing when study time is available.}

| Day | Available Hours | Committed Hours | Notes |
|-----|-----------------|-----------------|-------|
| Monday | {e.g., 6:00 PM - 10:00 PM} | {e.g., 8:00 AM - 5:00 PM work} | {Notes} |
| Tuesday | {Available hours} | {Committed hours} | {Notes} |
| Wednesday | {Available hours} | {Committed hours} | {Notes} |
| Thursday | {Available hours} | {Committed hours} | {Notes} |
| Friday | {Available hours} | {Committed hours} | {Notes} |
| Saturday | {Available hours} | {Committed hours} | {Notes} |
| Sunday | {Available hours} | {Committed hours} | {Notes} |

**Total Weekly Study Hours Available:** {X hours}

### Fixed Commitments

{Regular commitments that affect study scheduling.}

| Commitment | Days/Times | Priority | Notes |
|------------|------------|----------|-------|
| {Work} | {e.g., M-F 8 AM - 5 PM} | {High/Medium/Low} | {e.g., "Flexible for important deadlines"} |
| {Other classes} | {Days/times} | {Priority} | {Notes} |
| {Family obligations} | {Days/times} | {Priority} | {Notes} |
| {Exercise/health} | {Days/times} | {Priority} | {Notes} |

---

## Technology Profile
<!-- anchor: #technology-profile -->

{Josh's technology access and constraints.}

| Resource | Availability | Notes |
|----------|--------------|-------|
| **Devices** | {Laptop / Desktop / Both / Mobile} | {e.g., "MacBook Pro, iPhone for notifications"} |
| **Internet Reliability** | {Reliable / Intermittent / Limited} | {e.g., "Reliable at home and campus"} |
| **Software Access** | {List key software} | {e.g., "Microsoft Office, R Studio, Zoom"} |

---

## Known Challenges
<!-- anchor: #known-challenges -->

{Areas where Josh anticipates needing additional support or practice.}

- {Challenge 1, e.g., "Statistical analysis - need extra practice with regression"}
- {Challenge 2, e.g., "Time management during group projects"}
- {Challenge 3, e.g., "Public speaking for presentations"}

---

## Group Project Context
<!-- anchor: #group-project-context -->

{Information about Josh's group project team and responsibilities. Personal names are replaced with placeholders.}

### Project Overview

| Field | Value |
|-------|-------|
| **Project ID** | {PROJ-FINAL or GP01} |
| **Project Title** | {Project title} |
| **Team Name** | {Team name if assigned} |
| **Team Size** | {Number of members} |

### Team Structure

| Role | Member ID | Responsibilities |
|------|-----------|------------------|
| {Team Lead} | {Member 01 / Josh} | {e.g., "Coordination, final review, presentation lead"} |
| {Research Lead} | {Member 02} | {e.g., "Literature review, data collection"} |
| {Analysis Lead} | {Member 03} | {e.g., "Data analysis, visualization"} |
| {Writing Lead} | {Member 04} | {e.g., "Report drafting, editing"} |

**Josh's Role:** {Specific role and primary responsibilities}

### Communication Norms

{How the team has agreed to communicate.}

| Aspect | Agreement |
|--------|-----------|
| **Primary Channel** | {e.g., "Slack group chat"} |
| **Meeting Frequency** | {e.g., "Weekly Sunday 7 PM via Zoom"} |
| **Response Expectation** | {e.g., "Respond within 24 hours"} |
| **Document Sharing** | {e.g., "Google Drive shared folder"} |
| **Decision Making** | {e.g., "Majority vote; escalate to instructor if deadlocked"} |

### Milestone Ownership

{Josh's responsibilities for each project milestone.}

| Milestone ID | Due Date (Display) | Due Date (ISO) | Josh's Deliverables | Status |
|--------------|-------------------|----------------|---------------------|--------|
| MS01 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {e.g., "Draft team charter"} | {Not started / In progress / Complete} |
| MS02 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Josh's specific deliverables} | {Status} |
| MS03 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Josh's specific deliverables} | {Status} |
| MS04 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Josh's specific deliverables} | {Status} |

### Team Challenges and Agreements

{Any known team dynamics or agreements relevant to pacing and support.}

- {e.g., "Member 03 has limited availability in Week 8 - Josh covering additional analysis"}
- {e.g., "Team agreed to have drafts ready 48 hours before milestone deadlines for review"}

---

## Index References
<!-- anchor: #index-references -->

This file contains the following sections indexed for retrieval:

| Section Anchor | Section Title | Entity IDs |
|----------------|---------------|------------|
| #metadata | Metadata | — |
| #student-identification | Student Identification | — |
| #learning-preferences | Learning Preferences | — |
| #time-constraints | Time Constraints | — |
| #technology-profile | Technology Profile | — |
| #known-challenges | Known Challenges | — |
| #group-project-context | Group Project Context | {PROJECT_ID} |
| #index-references | Index References | — |

---

**END OF STUDENT KNOWLEDGE TEMPLATE**