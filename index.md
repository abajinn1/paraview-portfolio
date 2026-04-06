# Scientific Visualization Portfolio in ParaView

**Author:** Ryan DeJong  
**HAI:** 6e2713977c88@handshakecommunity.ai

This portfolio presents scientific visualization case studies built in ParaView using real technical data, command-line preprocessing, and visual refinement. The goal is to turn raw scientific or engineering outputs into clearer reviewer-facing assets for comparison, interpretation, and AI-adjacent evaluation workflows.

---

## Jump to project
- [Project 1: Reservoir Model Refinement in ParaView](#project-1-reservoir-model-refinement-in-paraview)
- [Project 2: CFD Visualization Refinement in ParaView](#project-2-cfd-visualization-refinement-in-paraview)

---

## Project 1: Reservoir Model Refinement in ParaView
**Tools:** PowerShell, Python, `em2ex`, ParaView  
**Dataset:** Public Norne reservoir model components from the OPM data repository  
**Output format:** Exodus II (`.e`)

This case study shows how a public reservoir model was assembled from multi-file engineering inputs, converted to Exodus II through a repeatable command-line workflow, and refined in ParaView into clearer reviewer-facing assets.

### Featured final assets

These are the primary reviewer-facing ParaView outputs for Project 1. Together they show the model exterior, property comparison, and internal structure inspection.

<p>
  <a href="assets/project1-norne/p1-05-norne-final-poro-view.png" target="_blank" rel="noopener noreferrer">
    <img src="assets/project1-norne/p1-05-norne-final-poro-view.png" alt="Norne reservoir model porosity view" width="49%">
  </a>
  <a href="assets/project1-norne/p1-06-norne-final-permx-view.png" target="_blank" rel="noopener noreferrer">
    <img src="assets/project1-norne/p1-06-norne-final-permx-view.png" alt="Norne reservoir model permeability view" width="49%">
  </a>
</p>

<p>
  <a href="assets/project1-norne/p1-07-norne-clip-or-slice-view.png" target="_blank" rel="noopener noreferrer">
    <img src="assets/project1-norne/p1-07-norne-clip-or-slice-view.png" alt="Norne reservoir model internal slice view" width="49%">
  </a>
  <a href="assets/project1-norne/p1-09-norne-slice-plus-plot-over-line-analysis.png" target="_blank" rel="noopener noreferrer">
    <img src="assets/project1-norne/p1-09-norne-slice-plus-plot-over-line-analysis.png" alt="Norne reservoir model slice plus plot over line analysis" width="49%">
  </a>
</p>

### What this project demonstrates

- Use of a real public reservoir engineering dataset
- Command-line model assembly and format conversion
- ParaView refinement of meaningful reservoir properties on the same structure
- Visual outputs supported by lightweight numeric analysis

### Problem

Public reservoir models are often distributed as multi-file engineering inputs, not reviewer-ready visualization assets.

### Objective

Assemble the source components, convert the model into a ParaView-readable format, and produce a compact set of clearer technical outputs for review and comparison.

### Data source and model assembly

This project used the public Norne reservoir case. The source model was organized as separate engineering components, including the structural grid, active-cell mask, porosity, and permeability. A short command-line assembly step was used to combine those components into a visualization-oriented input before conversion.

<a href="assets/project1-norne/p1-02-norne-source-files-console.png" target="_blank" rel="noopener noreferrer"><img src="assets/project1-norne/p1-02-norne-source-files-console.png" alt="Norne source files used for portfolio assembly"></a>

### Command-line workflow highlights

A short command-line workflow was used to assemble the source components and convert the model into a ParaView-readable Exodus II file.

```powershell
@"
SPECGRID
46 112 22 1 F /
INCLUDE
./INCLUDE/GRID/IRAP_1005.GRDECL /
INCLUDE
./INCLUDE/GRID/ACTNUM_0704.prop /
INCLUDE
./INCLUDE/PETRO/PORO_0704.prop /
INCLUDE
./INCLUDE/PETRO/PERM_0704.prop /
"@ | Set-Content .\NORNE_PORTFOLIO.grdecl
```

This created the assembled Norne input used for conversion.

```powershell
py em2ex.py -f NORNE_PORTFOLIO.grdecl
```

This produced the ParaView-readable Exodus II output.

<a href="assets/project1-norne/p1-03-norne-command-line-workflow-and-analysis.png" target="_blank" rel="noopener noreferrer"><img src="assets/project1-norne/p1-03-norne-command-line-workflow-and-analysis.png" alt="Norne command line workflow and analysis"></a>

### Initial loaded state

This screenshot shows the converted reservoir model immediately after loading in ParaView, before property-based refinement. The structure is visible, but the default view is not yet strong for fast reviewer-facing interpretation.

<a href="assets/project1-norne/p1-04-norne-initial-loaded-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/project1-norne/p1-04-norne-initial-loaded-view.png" alt="Norne initial loaded state"></a>

### Final curated property views

#### Porosity view (`poro`)

This was selected as the primary reviewer-facing view because it shows property variation clearly while preserving the reservoir’s layered and faulted structure.

<a href="assets/project1-norne/p1-05-norne-final-poro-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/project1-norne/p1-05-norne-final-poro-view.png" alt="Norne porosity view"></a>

#### Permeability view (`permx`)

This view shows a second reservoir property on the same structure. It reads as more technical and works well as a comparison view beside `poro`.

<a href="assets/project1-norne/p1-06-norne-final-permx-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/project1-norne/p1-06-norne-final-permx-view.png" alt="Norne permeability x view"></a>

#### Internal structure inspection

This slice view was included as a diagnostic interpretation image. It exposes internal layering and fault-related offsets that are less obvious from the exterior alone.

<a href="assets/project1-norne/p1-07-norne-clip-or-slice-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/project1-norne/p1-07-norne-clip-or-slice-view.png" alt="Norne internal slice view"></a>

### Console-assisted analysis

Lightweight console analysis was used to support view selection with actual scalar behavior, not appearance alone.

The converted model contains **44,927 active cells**.

For `poro`, the values are comparatively balanced and visually readable across the active model:
- Min: `0.0942`
- Max: `0.3473`
- Mean: `0.2421`
- Median: `0.2447`

For `permx`, the values span a much wider and more skewed range, making it a stronger technical comparison view:
- Min: `0.3221`
- Max: `3996.5476`
- Mean: `388.9713`
- Median: `209.9135`

### Slice-linked line sampling

This view pairs an internal `poro` slice with a sampled line profile to connect visual structure to extracted quantitative behavior. The cross-section exposes internal layering and fault offsets, while the accompanying plot shows how sampled values vary along the selected path through the model.

<a href="assets/project1-norne/p1-09-norne-slice-plus-plot-over-line-analysis.png" target="_blank" rel="noopener noreferrer"><img src="assets/project1-norne/p1-09-norne-slice-plus-plot-over-line-analysis.png" alt="Norne slice plus plot over line analysis"></a>

### Why these views were selected

These views were selected to balance readability, technical depth, and scanability. The `poro` view works best as the lead asset, `permx` works best as the technical comparison view, and the slice view shows internal interpretation rather than exterior rendering alone.

### AI-adjacent relevance

This workflow is relevant to AI-adjacent scientific asset development because it combines repeatable preprocessing, structured visualization, and compact numeric interpretation. Outputs like these can support review, comparison, labeling, evaluation, and human-in-the-loop interpretation workflows.

### Outcome

The result is a reviewer-facing case study built from a real public reservoir model. It demonstrates command-line preparation, format conversion, ParaView-based property refinement, and analysis tied to the underlying scalar data.

---

## Project 2: CFD Visualization Refinement in ParaView
**Tool:** ParaView  
**Dataset:** Official ParaView testing data, `disk_out_ref.ex2`

### Overview

This case study shows how a raw CFD dataset was refined in ParaView into clearer reviewer-facing scientific assets.

### What this project demonstrates

- Refinement of a raw scientific dataset into clearer technical outputs
- Use of color mapping, slicing, contouring, and stream tracing in ParaView
- Creation of multiple reviewer-facing deliverables from one source dataset
- Outputs that support AI-adjacent review, comparison, and interpretation workflows

### Featured final assets

These final deliverables were selected because they most clearly improve interpretability over the default loaded view.

### Velocity-mapped visuals

This final asset shows velocity variation clearly while preserving the object’s overall 3D form.

<a href="assets/10-final-velocity-collage.png" target="_blank" rel="noopener noreferrer"><img src="assets/10-final-velocity-collage.png" alt="Featured final asset velocity mapped view"></a>

### Slice-based internal inspection

This final asset makes internal variation easier to inspect than the exterior-only views.

<a href="assets/12-final-slice-collage.png" target="_blank" rel="noopener noreferrer"><img src="assets/12-final-slice-collage.png" alt="Featured final asset slice based internal inspection"></a>

### Stream tracer refinement

This final asset makes flow behavior more explicit across multiple viewing angles.

<a href="assets/09-final-stream-tracer-collage.png" target="_blank" rel="noopener noreferrer"><img src="assets/09-final-stream-tracer-collage.png" alt="Featured final asset stream tracer refinement"></a>

### Problem

The default loaded view did not clearly communicate internal flow structure or variable patterns.

### Objective

Produce a compact set of clearer scientific visualization outputs for review, comparison, and interpretation.

### Workflow

- Inspect the default loaded view
- Refine the camera angle for better feature visibility
- Apply velocity-based color mapping
- Use slicing to expose internal structure
- Use contouring to compare a second scalar field
- Use stream tracing to make flow paths more explicit

### Outcome

The result is a compact set of refined technical assets that improve interpretability over the default loaded view.

### AI relevance

These outputs are relevant to AI-adjacent workflows because they support review, comparison, evaluation, and human-in-the-loop interpretation.

### Supporting workflow visuals

#### 1. Initial dataset state

This screenshot shows the dataset in its default loaded state before refinement.

<a href="assets/01-raw-dataset-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/01-raw-dataset-view.png" alt="Initial dataset state"></a>

#### 2. Viewpoint refinement for feature visibility

The camera was reoriented to a stronger top-facing view so variable structure became easier to read.

<a href="assets/02-raw-dataset-plus-Z-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/02-raw-dataset-plus-Z-view.png" alt="Top view refinement"></a>

#### 3. Velocity-mapped view

This view applies the dataset’s `V` field for color mapping, making scalar variation visible instead of leaving the dataset as a plain surface.

<a href="assets/02-colored-by-velocity.png" target="_blank" rel="noopener noreferrer"><img src="assets/02-colored-by-velocity.png" alt="Velocity-mapped view"></a>

#### 4. Slice-based internal inspection

This slice view exposes internal field variation that is not visible from the exterior alone.

<a href="assets/04-slice-plus-x-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/04-slice-plus-x-view.png" alt="Slice-based internal inspection"></a>

#### 5. Slice orientation context

This isometric view shows the position of the slice plane within the full geometry.

<a href="assets/05-slice-isometric-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/05-slice-isometric-view.png" alt="Slice orientation context"></a>

#### 6. Pressure contour extraction

This contour view uses the `Pres` field to extract a second scalar-based result for comparison.

<a href="assets/06-pressure-contour-isometric.png" target="_blank" rel="noopener noreferrer"><img src="assets/06-pressure-contour-isometric.png" alt="Pressure contour extraction"></a>

#### 7. Stream tracer refinement

This stream tracer result uses a point-cloud seed setup to make directional flow behavior more explicit.

<a href="assets/07-stream-tracer-point-cloud.png" target="_blank" rel="noopener noreferrer"><img src="assets/07-stream-tracer-point-cloud.png" alt="Stream tracer refinement"></a>