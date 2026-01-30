# Relevance and Exclusion Report
**Agent Build Scope**: Single course, single term, single student (Josh)  
**Report Date**: 2026-01-25  
**Purpose**: Categorize information across all attachments; recommend exclusion/anonymization rules

---

## Information Categorization

### ESSENTIAL (Required for Agent Functionality)

**Course Structure & Policy**:
- Course title, number, credits
- Instructor name and contact (office hours, email)
- Term dates (start, end, key deadlines)
- Grading policy (weights, components, scale)
- Attendance and participation policies
- Late work policy
- Academic integrity policy
- Required technology/tools

**Schedule & Assignments**:
- Module/week numbers and topics
- Assignment titles, types, due dates, point values
- Exam dates and coverage
- Reading assignments with specific page numbers or chapters
- Submission requirements and formats
- Prerequisites and dependencies between assignments

**Student Profile Core**:
- Student name (Josh)
- Timezone (America/Chicago)
- Preferred communication style
- Learning preferences and constraints
- Technology access and preferences
- Time management constraints (work schedule, other commitments)

---

### HELPFUL (Enhances Agent Performance)

**Course Context**:
- Learning objectives per module
- Topic descriptions and summaries
- Suggested study strategies
- Optional resources and supplementary materials
- Course philosophy or teaching approach

**Student Context**:
- Writing style preferences (see Writing_Style_Profile_Josh.md)
- Previous course experience in subject area
- Specific goals for the course
- Preferred assignment planning approach
- Note-taking preferences

**Assignment Support**:
- Rubrics and grading criteria
- Example submissions or templates
- Common mistakes to avoid
- Success criteria and expectations
- Deliverable checklists

**Group Project Information** (when applicable):
- Project scope and deliverables
- Milestone schedule
- Individual role and responsibilities
- Communication norms and meeting schedule
- Conflict resolution process

---

### IRRELEVANT (Can Be Safely Excluded)

**Institutional Boilerplate**:
- University mission statements
- Generic disability accommodation language (keep only course-specific procedures)
- Standard honor code text (keep only course-specific expectations)
- Accreditation information
- Department administrative details

**Redundant Information**:
- Information duplicated verbatim across multiple sections
- Historical context not relevant to current term
- Previous semester details

**Non-Operational Metadata**:
- PDF page numbers
- Document version history (unless impacts current requirements)
- Creation timestamps of source documents
- File size information from tree structure
- Folder depth levels

---

### HARMFUL TO RETRIEVAL (Must Be Excluded or Transformed)

**Personal Identifying Information**:
- **Group member full names** (CRITICAL EXCLUSION)
  - Current practice: MGMT-8001 lists "Ben Shapiro, Julia Jankowicz, Siddharth Venkataramakrishnan, Gretchen Whitmer"
  - Current practice: IDSC-4444 lists "Nidhi Upadhyay, Rohan Nimbalkar"
  - **Harm**: Privacy violation, no operational value for agent, increases token usage
  - **Replacement**: Use role-based placeholders (Member 01, Member 02) or role titles (Data Analyst, Project Lead)

**Unstructured Prose in Place of Structured Data**:
- Long paragraph descriptions of assignments when structured lists would suffice
- Narrative schedule descriptions instead of tabular formats
- **Harm**: Reduces retrieval accuracy, increases parsing errors

**Ambiguous Date Formats**:
- "1/5" (unclear: Jan 5 or May 1?)
- "Next Tuesday" (context-dependent)
- Relative dates without anchor
- **Harm**: Causes date calculation errors, timezone confusion

**Duplicate Content with Variations**:
- Same assignment described slightly differently in schedule vs assignment section
- **Harm**: Agent may cite conflicting information, reducing trust

**Inconsistent Terminology**:
- "Quiz" vs "Assessment" vs "Check-in" for same thing
- "Module" vs "Week" vs "Unit"
- **Harm**: Reduces recall in retrieval, causes missed information

**Nested References Without Context**:
- "See syllabus for details" without section anchor
- "Refer to module materials" without file path
- **Harm**: Breaks retrieval chain, forces guessing

---

## Exclusion and Anonymization Policy

### Personal Information Redaction Rules

**RULE 1: Group Member Names**
- **Action**: Remove all personal names from group project information
- **Replacement Pattern**: 
  ```
  Member 01 (Role: [role if specified])
  Member 02 (Role: [role if specified])
  Member 03 (Role: [role if specified])
  ```
- **Keep**: Role assignments, responsibilities, contact methods (Slack, email type but not addresses)
- **Remove**: Full names, email addresses, phone numbers, social media handles

**RULE 2: Instructor Personal Details**
- **Keep**: Name, title, office hours, official university contact (email, office number)
- **Remove**: Personal phone, personal email, home address, personal anecdotes

**RULE 3: Student Personal Details** (for Josh)
- **Keep**: First name only, timezone, relevant constraints
- **Remove**: Last name, address, specific employer name, specific family details

### Information Minimization Rules

**RULE 4: Boilerplate Reduction**
- Extract only course-specific procedures from standard policies
- Replace generic accommodation language with: "See course_knowledge.policies.accommodations for specific procedures"
- Remove repeated honor code text; keep only course-specific academic integrity expectations

**RULE 5: Duplicate Elimination**
- Maintain single source of truth for each fact
- If assignment appears in both schedule and assignments section: keep detailed version in assignments, reference by ID in schedule
- Remove redundant topic descriptions

**RULE 6: Metadata Stripping**
- Remove file paths from module tree except where needed for retrieval
- Remove file sizes and timestamps
- Remove PDF page numbers and formatting artifacts

**RULE 7: Ambiguity Removal**
- Convert all relative dates to absolute dates with display_date and iso_date
- Standardize terminology (create glossary if needed)
- Replace vague references ("later", "previous module") with specific IDs

### Content Transformation Rules

**RULE 8: Structure Over Prose**
- Convert paragraph descriptions to structured sections with headers
- Use tables for schedules and assignment lists
- Use bullet lists for requirements and deliverables

**RULE 9: Anchor Addition**
- Add unique section IDs to all headers for retrieval targeting
- Format: `### Assignment 3: Data Analysis {#assignment-03-data-analysis}`

**RULE 10: Explicit Unknowns**
- Replace missing information with explicit markers
- Use: `TBD` (to be determined), `Not Specified`, `See [source] for updates`
- Never guess or invent information

---

## Recommended Implementation Workflow

### Step 1: Scan for Personal Information
1. Search all course materials for full names
2. Identify group rosters, contact lists, example submissions with names
3. Create redaction log: what was found, what was removed, what was replaced

### Step 2: Apply Anonymization
1. Replace group member names with Member 01, Member 02, etc.
2. Preserve only operationally necessary information (roles, responsibilities, communication norms)
3. Validate no personal identifiers remain

### Step 3: Remove Boilerplate
1. Identify repeated institutional language
2. Extract course-specific procedures
3. Remove or summarize generic content

### Step 4: Eliminate Duplicates
1. Map where same information appears multiple times
2. Choose canonical location (highest detail, most structured)
3. Replace duplicates with references using IDs

### Step 5: Standardize Format
1. Convert dates to display_date + iso_date pairs
2. Standardize terminology throughout
3. Add section anchors for retrieval

### Step 6: Validate Minimization
1. Check that every included item serves operational purpose
2. Verify all excluded items documented in this report
3. Confirm no information loss of essential content

---

## Specific Findings from Current Files

### MGMT-8001-2024-SP.student_knowledge.md
**HARMFUL - Must Redact**:
```
Group Members:
- Ben Shapiro (ben.shapiro@tuck.dartmouth.edu)
- Julia Jankowicz (julia.jankowicz@tuck.dartmouth.edu)
- Siddharth Venkataramakrishnan (siddharth.venkataramakrishnan@tuck.dartmouth.edu)
- Gretchen Whitmer (gretchen.whitmer@tuck.dartmouth.edu)
```

**REPLACEMENT**:
```
Group Members:
- Member 01 (Role: [if specified])
- Member 02 (Role: [if specified])
- Member 03 (Role: [if specified])
- Member 04 (Role: [if specified])

Communication: Team uses email and scheduled meetings
```

### IDSC-4444-2024-FA.student_knowledge.md
**HARMFUL - Must Redact**:
```
- Partner: Nidhi Upadhyay
- Partner: Rohan Nimbalkar
```

**REPLACEMENT**:
```
- Partner 01
- Partner 02

Partnership approach: [keep any relevant working norms]
```

### All Course Knowledge Files
**IRRELEVANT - Can Remove**:
- Repeated "Students with disabilities" boilerplate (keep course-specific procedure only)
- PDF metadata and page count information
- File creation dates

**HARMFUL - Must Transform**:
- Inconsistent date formats → Apply display_date + iso_date standard
- Narrative assignment descriptions → Convert to structured sections
- Missing assignment IDs → Generate deterministic IDs

---

## Impact Assessment

### Token Efficiency Gains
**Before Minimization** (estimated):
- MGMT-8001 course_knowledge.md: ~12,000 tokens
- Group member details: ~200 tokens
- Redundant boilerplate: ~800 tokens
- Duplicate assignments: ~600 tokens

**After Minimization** (estimated):
- MGMT-8001 course_knowledge.md: ~10,000 tokens (16% reduction)
- Privacy compliant: 100% names removed
- Retrieval accuracy: Improved through structure

### Retrieval Accuracy Improvements
- Structured sections increase anchor targeting success
- Standardized terminology reduces missed information
- Explicit unknowns prevent hallucination
- Single source of truth eliminates contradictions

### Privacy Compliance
- Zero personal identifiers of non-student individuals
- Student information limited to operational necessities
- Clear audit trail of what was redacted

---

## Future Minimization Policy

**For Every New Course Build**:

1. **Privacy Scan**:
   - Search for: full names, email addresses (@), phone numbers
   - Flag all group rosters and contact lists
   - Apply Member 01-XX replacement pattern

2. **Boilerplate Check**:
   - Identify institutional standard language
   - Keep only course-specific details
   - Reference standard policies by name only

3. **Duplicate Detection**:
   - Map information across sections
   - Choose canonical location
   - Replace with ID references

4. **Structure Conversion**:
   - Transform prose to structured sections
   - Add anchor IDs
   - Standardize dates and terminology

5. **Validation**:
   - Every included item must answer: "Does the agent need this to help Josh?"
   - If answer is no → exclude or minimize
   - If answer is yes → include in structured format only

**Documentation Requirement**:
- Every exclusion must be logged
- Every anonymization must be documented
- Every transformation must preserve meaning

---

## Exceptions and Edge Cases

**Exception 1: Instructor Names**
- **Keep**: Instructor names are public information and operationally necessary
- **Format**: Full name + title on first reference, last name only thereafter

**Exception 2: Public Figures in Examples**
- If course materials reference public figures as examples (case studies, etc.), these may be kept
- Group member names are NOT public figures for this purpose

**Exception 3: Published Authors**
- Reading assignments may include author names for citation purposes
- Keep author names for required readings

**Edge Case 1: Student is Group Project Lead**
- If Josh has specific coordination responsibilities, document the structure without naming other members
- Focus on: milestone schedule, deliverable ownership, communication cadence

**Edge Case 2: Course References External Teams**
- If assignment requires interaction with other teams, use Team A, Team B notation
- Avoid individual names

---

## Summary Recommendations

**Critical Actions**:
1. Implement mandatory personal information redaction for all group rosters
2. Standardize date formats to display_date + iso_date pairs
3. Eliminate duplicate content through ID-based referencing
4. Convert narrative descriptions to structured sections with anchors
5. Remove all non-operational boilerplate

**Quality Improvements**:
1. Add section IDs for precise retrieval targeting
2. Standardize terminology across all files
3. Mark all unknowns explicitly (no guessing)
4. Validate every included item serves operational purpose

**Compliance**:
1. Zero tolerance for personal identifying information of non-student individuals
2. Audit trail required for all redactions
3. Policy applies to all future course builds

**Expected Outcome**:
- 10-20% token reduction
- Improved retrieval accuracy through structure
- Full privacy compliance
- Maintainable, reusable system