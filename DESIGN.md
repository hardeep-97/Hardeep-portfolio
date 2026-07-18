---
name: Hardeep Shiyani Portfolio
description: A direct, evidence-first portfolio for a Software and DevOps Developer.
colors:
  midnight-infrastructure: "#010e1b"
  deep-system-navy: "#09203a"
  raised-system-navy: "#102d4c"
  signal-coral: "#ec5252"
  cloud-white: "#ffffff"
  soft-white: "#dee2e6"
  technical-muted: "#9cb4ca"
typography:
  display:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(3rem, 6.8vw, 5.75rem)"
    fontWeight: 700
    lineHeight: 0.99
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(2.1rem, 4.4vw, 4rem)"
    fontWeight: 700
  title:
    fontFamily: "Archivo, sans-serif"
    fontSize: "20px"
    fontWeight: 700
  body:
    fontFamily: "Source Sans 3, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Source Sans 3, sans-serif"
    fontSize: "14px"
    fontWeight: 600
rounded:
  square: "0"
  control: "4px"
  button: "6px"
  panel: "10px"
  card: "12px"
  pill: "20px"
  circle: "50%"
spacing:
  xs: "6px"
  sm: "10px"
  md: "20px"
  lg: "24px"
  section: "30px"
components:
  button-primary:
    backgroundColor: "{colors.signal-coral}"
    textColor: "{colors.cloud-white}"
    rounded: "{rounded.button}"
    padding: "11px 20px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.soft-white}"
    rounded: "{rounded.button}"
    padding: "11px 20px"
  artifact-panel:
    backgroundColor: "{colors.deep-system-navy}"
    textColor: "{colors.cloud-white}"
    rounded: "{rounded.card}"
    padding: "22px"
---

# Design System: Hardeep Shiyani Portfolio

## 1. Overview

**Creative North Star: "The Reliable Engineering Console"**

The portfolio should feel like a dependable technical workspace translated into a public-facing Resume: dark, focused, and easy to scan. Midnight and navy surfaces establish seriousness; Signal Coral directs attention toward navigation, links, project actions, and key states. The system is practical, confident, and direct rather than theatrical.

Information density is welcome when it helps a recruiter verify experience, but hierarchy must remain obvious. Project screenshots and measurable outcomes provide the visual interest. The system explicitly rejects flashy or slow animation, generic claims without evidence, crowded skill-logo walls, hidden Resume or contact paths, Tech-Lead-only positioning, and template-like or obviously AI-generated visuals.

**Key Characteristics:**

- Dark, high-contrast surfaces with a single dominant action signal.
- Compact recruiter-friendly typography and navigation.
- Real project imagery and evidence before decoration.
- Flat structure at rest with elevation reserved for interaction.
- Direct routes to contact, Resume, LinkedIn, and project proof.

## 2. Colors

The palette reads as infrastructure at night: deep blue-black foundations, legible white text, and coral signals used to identify action.

### Primary

- **Signal Coral:** The main interaction signal for links, active navigation, project controls, tags, and focus-worthy moments. Its rarity gives it authority.

### Neutral

- **Midnight Infrastructure:** The page foundation and full-viewport background.
- **Deep System Navy:** The primary raised surface for cards, contact blocks, and content containers.
- **Raised System Navy:** A slightly brighter layer for hovered or emphasized navy surfaces.
- **Cloud White:** Primary text and high-contrast icon color.
- **Soft White:** Secondary heading and icon color where full white would be too sharp.
- **Technical Muted:** Supporting project copy, dates, and metadata.

### Named Rules

**The Signal Rule.** Signal Coral marks an action, active state, or meaningful technical label; it is never ambient decoration.

**The One-Signal Rule.** Signal Coral is the only saturated interface accent.

## 3. Typography

**Display Font:** Archivo (with sans-serif fallback)  
**Body Font:** Source Sans 3 (with sans-serif fallback)  
**Label Font:** Source Sans 3 (with sans-serif fallback)

**Character:** Archivo gives headings a precise, workmanlike authority while Source Sans 3 keeps dense technical evidence highly readable. The contrast feels engineered rather than decorative.

### Hierarchy

- **Display** (700, fluid 48–92px, 0.99): First-screen positioning only.
- **Headline** (700, fluid 34–64px): Major section statements.
- **Title** (700, 18–20px): Project names, contact headings, and content-group titles.
- **Body** (400, 16px, 1.65): Project narratives and supporting evidence; prose should remain within 65–75 characters per line where layout allows.
- **Label** (600, 11–14px): Navigation, tags, dates, and short metadata. Uppercase is limited to compact tags or true labels.

### Named Rules

**The Recruiter Scan Rule.** A heading communicates role, project, or evidence; it never exists merely to decorate a section.

**The Two-Family Rule.** Archivo carries identity and hierarchy; Source Sans 3 carries every reading and interface role.

## 4. Elevation

The system is flat. Depth comes from navy tonal layers, borders, and image scale rather than drop shadows. Static and interactive containers remain shadowless.

### Named Rules

**The Shadowless Rule.** Use tonal contrast, boundaries, and restrained image movement for depth. Decorative drop shadows are prohibited.

## 5. Components

Components are compact, technical, and evidence-first. Controls signal function clearly; project content receives more visual weight than chrome.

### Buttons

- **Shape:** Gently squared corners (6px) and a minimum 50px touch height.
- **Primary:** Signal Coral fill with Cloud White text and 11px × 20px padding.
- **Hover / Focus:** Primary controls brighten slightly and move up by 2px on hover. Every control uses a 3px high-contrast `:focus-visible` outline.
- **Secondary / Ghost:** Transparent with a quiet neutral border and Soft White text.

### Chips

- **Style:** Project facts use transparent backgrounds, muted text, a quiet neutral border, pill radius, and 5px × 10px padding.
- **State:** Tags are descriptive metadata, not buttons. They do not animate or imply selection.

### Project Rows / Containers

- **Corner Style:** Project images use 6px corners; the featured artifact uses a restrained 12px radius.
- **Background:** Project rows sit directly on Deep System Navy without card shells.
- **Shadow Strategy:** Always shadowless.
- **Border:** Quiet horizontal rules separate evidence without boxing every item.
- **Internal Padding:** Responsive section rhythm provides 54–92px around each project row.

### Navigation

Desktop navigation uses 14px Source Sans 3 labels, 28px gaps, Soft White at rest, and a short Signal Coral underline for hover and active states. On mobile it becomes a full-width navy panel with 52px tap targets. The Resume remains a bordered action.

### Featured Artifact

The signature hero component presents hTunnel as a real engineering artifact: source status, current year, product screenshot, one-sentence explanation, and a direct source link. The image may scale by 2.5% on hover; content stays fully visible without animation.

## 6. Do's and Don'ts

### Do:

- **Do** make employability, role breadth, and contact paths obvious in the first screen.
- **Do** use real project screenshots and measurable evidence as the primary visual material.
- **Do** reserve Signal Coral for actions, active states, and meaningful labels.
- **Do** keep project copy concise, outcome-oriented, and readable at 16px with 1.65 line height.
- **Do** preserve keyboard navigation, visible focus, AA contrast, useful alt text, and reduced-motion behavior.

### Don't:

- **Don't** add flashy or slow animation.
- **Don't** use generic claims without evidence.
- **Don't** create crowded skill-logo walls; prioritize role-relevant skills with context.
- **Don't** hide Resume or contact paths.
- **Don't** position Hardeep only as a Tech Lead.
- **Don't** use template-like or obviously AI-generated visuals.
- **Don't** add gradient text, decorative glassmorphism, repeated section eyebrows, or identical icon-card grids.
- **Don't** add decorative drop shadows to static or interactive surfaces.
