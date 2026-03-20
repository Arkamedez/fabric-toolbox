# SpartanNash — UI Design Specification

> **Version:** 1.0  
> **Date:** March 20, 2026  
> **Purpose:** Developer reference for building applications, dashboards, and reports aligned with the SpartanNash brand identity.

---

## Document History
* **v1.0** (March 20, 2026): Initial UI design specification migrated from legacy documentation to modern format.

---

## 1. Corporate Color Palette

These are the **primary brand colors** used for UI chrome, headers, navigation, logos, and body text.

| Role | Name | Hex | Usage |
|---|---|---|---|
| **Primary** | SPTN Dark Green | `#006A52` | Visual headers, primary titles, navigation |
| **Secondary** | SPTN Mid Green | `#43B02A` | Section headers, primary actions |
| **Tertiary** | SPTN Light Green | `#A4D65E` | Secondary elements, positive indicators |
| **Background** | White | `#FFFFFF` | Page backgrounds, card surfaces |
| **Neutral** | Dark Gray | `#525051` | Labels, axis text, informational text |

### Surface & Neutral Colors

| Name | Hex | Usage |
|---|---|---|
| Page Background | `#F2F2F2` | Canvas / outer page area behind cards |
| Card Surface | `#FFFFFF` | Visual container backgrounds |
| Divider / Grid | `[TO BE FILLED BY SPTN]` | Table gridlines, borders, separators |
| Alternating Row | `[TO BE FILLED BY SPTN]` | Banded table rows for readability |

---

## 2. Data Visualization Palette

The **splash colors** are reserved for charts, graphs, and any visual requiring multiple distinct data series.

| Order | Name | Hex | Primary Use |
|---|---|---|---|
| 1 | Dark Green | `#006A52` | Default / first series |
| 2 | Mid Green | `#43B02A` | Second series |
| 3 | Light Green | `#A4D65E` | Third series |
| 4 | Gold | `#FFC72C` | Fourth series |
| 5 | Teal Gray | `#99C3BA` | Fifth series |
| 6 | Sage Green | `#8ED07F` | Sixth series |
| 7 | Pale Green | `#C8E69E` | Seventh series |
| 8 | Pale Gold | `#FFDD80` | Eighth series |

### Semantic Colors & Conditional Formatting

| Context | Color | Hex | Usage Notes |
|---|---|---|---|
| ✅ Good / Positive | Light Green | `#A4D65E` | KPIs hitting target, success states. |
| ⚠️ Neutral / Info | Blue | `#3D7AA9` | Informational callouts. |
| ❌ Bad / Negative | Red | `#EB1316` | Missing targets, errors. |

#### Conditional Formatting Scales
When using gradient fills for heatmaps or table backgrounds, use the following scale:
* Minimum: **Gold (`#FFBE0E`)**
* Center: **Orange (`#ED6102`)**
* Maximum: **Maroon (`#700017`)**

---

## 3. Typography

> [!IMPORTANT]
> **Arial** is the approved font family across all deliverables.

| Element | Font | Weight | Size | Color |
|---|---|---|---|---|
| **Visual Title** | Arial | Bold | 11px | `#006A52` |
| **Section Header** | Arial | Bold | 10.5px | `#43B02A` |
| **Body Text** | Arial | Regular | 10px | `#000000` |
| **Callout / KPI** | Arial | Bold | 10px | `#000000` |
| **Category Label** | Arial | Regular | 10px | `#525051` |
| **Column Heading** | Arial | Bold | 10px | `#000000` |
| **Group Headers** | Arial | Bold | 10px | `#000000` |

---

## 4. Component Specifications

### 4.1 Cards (KPI / Metric)

```
┌──────────────────────────┐
│  [Visual Title]          │  Arial Bold 11px #006A52
│                          │
│       1,234              │  Arial Bold 10px #000000
│    Category Label        │  Arial Regular 10px #525051
│                          │
└──────────────────────────┘
  Background: #FFFFFF
  Border: Solid #A1A1A1
  Border Radius: 16px
```

### 4.2 Tables & Matrix

```
┌──────────────┬────────────┬───────────┐
│  Column A    │  Column B  │  Column C │  Header: #000000 on #FFFFFF, Arial Bold 10px
|              |            |           |  (Underline/Outline [TO BE FILLED])
├──────────────┼────────────┼───────────┤
│  Data Row 1  │  value     │  value    │  Row: Arial 10px, #000000
│  Data Row 2  │  value     │  value    │
└──────────────┴────────────┴───────────┘
```

### 4.3 Slicers

| Element | Specification |
|---|---|
| Header text | Arial Bold 11px, `#006A52` |
| Background | `#FFFFFF` |
| Item text | Arial Regular 10px, `#000000` |

### 4.4 Navigation & Buttons

| State | Background | Text | Border |
|---|---|---|---|
| **Primary** | `[TO BE FILLED]` | `[TO BE FILLED]` | `[TO BE FILLED]` |
| **Primary Hover** | `[TO BE FILLED]` | `[TO BE FILLED]` | `[TO BE FILLED]` |

---

## 5. Spacing & Layout

| Token | Value | Usage |
|---|---|---|
| `padding-card` | `[TO BE FILLED]` | Inner padding for card visuals |
| `padding-page` | `[TO BE FILLED]` | Page margin |
| `gap-visual` | `[TO BE FILLED]` | Space between visuals |
| `border-radius` | 16px | Globally applied to visual borders |
| `border-weight` | 1px | Applied to visual containers |

---

## 6. Accessibility Notes
`[TO BE FILLED BY SPTN]`

---

## 7. Power BI Theme File
The companion Power BI theme JSON for SpartanNash is available at:
**[SpartanNash Theme.json](file:///C:/GIT/FUAM/themes/SpartanNash%20Theme.json)**

---

## 8. Quick Reference - Color Codes

| Category | Role / Element | Hex | Sample |
|---|---|---|---|
| **Corporate** | SPTN Dark Green | `#006A52` | ![#006A52](https://placehold.co/15x15/006A52/006A52.png) |
| | SPTN Mid Green | `#43B02A` | ![#43B02A](https://placehold.co/15x15/43B02A/43B02A.png) |
| | SPTN Light Green | `#A4D65E` | ![#A4D65E](https://placehold.co/15x15/A4D65E/A4D65E.png) |
| | SPTN Neutral | `#525051` | ![#525051](https://placehold.co/15x15/525051/525051.png) |
| **Semantic** | Good / Positive | `#A4D65E` | ![#A4D65E](https://placehold.co/15x15/A4D65E/A4D65E.png) |
| | Neutral / Info | `#3D7AA9` | ![#3D7AA9](https://placehold.co/15x15/3D7AA9/3D7AA9.png) |
| | Bad / Negative | `#EB1316` | ![#EB1316](https://placehold.co/15x15/EB1316/EB1316.png) |
| **Scale** | Maximum (Good) | `#700017` | ![#700017](https://placehold.co/15x15/700017/700017.png) |
| | Center (Neutral)| `#ED6102` | ![#ED6102](https://placehold.co/15x15/ED6102/ED6102.png) |
| | Minimum (Bad) | `#FFBE0E` | ![#FFBE0E](https://placehold.co/15x15/FFBE0E/FFBE0E.png) |
