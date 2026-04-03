# ParaView Portfolio
Ryan DeJong | 6e2713977c88@handshakecommunity.ai

## Project 1: Flow Field Refinement in ParaView

**Focus:** Scientific visualization asset refinement for AI-adjacent research workflows

### Project summary

This project uses ParaView to refine raw scientific simulation output into clearer, reviewer-ready visualization assets for AI-related research workflows.

### Status

In progress

### Dataset

- Source: Official ParaView testing data
- File: `disk_out_ref.ex2`

### Planned workflow

- Load raw simulation data
- Inspect available variables
- Create refined views using slice, clip, contour, and streamlines
- Export still images
- Optionally export a short animation

### AI relevance

These outputs are relevant to AI-adjacent research workflows because refined scientific visualizations can support asset review, quality evaluation, interpretation, and human-in-the-loop analysis.

### Assets

#### Raw dataset view
This screenshot shows the initial loaded state of the scientific dataset in ParaView before any refinement filters were applied or changing the view.

<a href="assets/01-raw-dataset-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/01-raw-dataset-view.png" alt="Raw dataset view"></a>

#### Orientation refinement (+Z view)
The default loaded view did not clearly expose the internal velocity structure, so the camera was reoriented to a +Z view to make the field variation more visible and interpretable.

<a href="assets/02-raw-dataset-plus-Z-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/02-raw-dataset-plus-Z-view.png" alt="+Z view"></a> 

#### Velocity-colored view
This view applies the dataset’s `V` field for color mapping, which introduces a first-pass scientific variable overlay instead of a neutral solid-color surface. This is a basic refinement step because it starts turning the raw geometry into a more interpretable technical asset.

<a href="assets/02-colored-by-velocity.png" target="_blank" rel="noopener noreferrer"><img src="assets/02-colored-by-velocity.png" alt="Velocity-colored view"></a>

#### Slice refinement (+X view)
This slice view cuts through the volume to expose internal field variation that is not visible from the default loaded view alone. Using a planar slice is a stronger refinement step than simple exterior coloring because it reveals structure inside the dataset and makes the technical pattern easier to inspect.

<a href="assets/04-slice-plus-x-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/04-slice-plus-x-view.png" alt="Slice refinement plus X view"></a>

#### Slice orientation context (isometric view)
This isometric view shows the slice plane in 3D context, which helps clarify where the cut is positioned inside the dataset. It supports the main slice result by making the orientation and geometry easier to understand at a glance.

<a href="assets/05-slice-isometric-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/05-slice-isometric-view.png" alt="Slice orientation context isometric view"></a>

#### Pressure contour view
This contour view uses the `Pres` field to extract a more meaningful scalar-based result than the constant velocity-magnitude contour. It adds a second refinement mode by showing how a different scientific variable can reveal structure across the dataset in a reviewer-friendly isometric view.

<a href="assets/06-pressure-contour-isometric.png" target="_blank" rel="noopener noreferrer"><img src="assets/06-pressure-contour-isometric.png" alt="Pressure contour isometric view"></a>

#### Stream tracer view
This stream tracer result uses a point-cloud seed setup to generate a fuller set of flow paths through the dataset than the earlier line-seed attempt. It is one of the strongest refinement outputs in the case study because it makes the flow structure more explicit and visually interpretable.

<a href="assets/07-stream-tracer-point-cloud.png" target="_blank" rel="noopener noreferrer"><img src="assets/07-stream-tracer-point-cloud.png" alt="Stream tracer point cloud view"></a>