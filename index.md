# ParaView Training Portfolio
Ryan DeJong | 6e2713977c88@handshakecommunity.ai

## Project 1: Flow Field Refinement in ParaView

**Focus:** Scientific visualization asset refinement for AI-adjacent research workflows

### Project summary

This project demonstrates a basic ParaView workflow for turning raw scientific simulation output into clearer, reviewer-ready visualization assets. The focus is on refinement, interpretability, and technical presentation rather than claiming model training or automated AI generation.

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

#### Set view direction to +Z 
Using the given tool, I changed the direction. The initial loaded state's view did not have the velocity variance necessary for the demonstration.

<a href="assets/02-raw-dataset-plus-Z-view.png" target="_blank" rel="noopener noreferrer"><img src="assets/02-raw-dataset-plus-Z-view.png" alt="+Z view"></a> 

#### Velocity-colored view
This view applies the dataset’s `V` field for color mapping, which introduces a first-pass scientific variable overlay instead of a neutral solid-color surface. This is a basic refinement step because it starts turning the raw geometry into a more interpretable technical asset.

<a href="assets/02-colored-by-velocity.png" target="_blank" rel="noopener noreferrer"><img src="assets/02-colored-by-velocity.png" alt="Velocity-colored view"></a>
