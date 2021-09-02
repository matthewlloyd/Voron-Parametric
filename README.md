# The Parametric Voron

This repository contains Fusion 360 reconstructions of various printed parts from the Voron printers (https://vorondesign.com/). Unlike the CAD files provided by the Voron team, which are essentially just STEP files in F3D format, these files have full parametric design history turned on, and are easy to edit.

This is a community effort and it may take months, or even years, to recreate the full set of parts. If you would like to contribute, feel free to open a pull request. Parts are organized per Voron release, with the same directory structure and naming conventions used by the original Voron parts.

For inspiration as to what this could eventually become, take a look at the Fusion 360 Models available for the Railcore project (https://railcore.org/). Every part is fully parametric with design history, and the parts are all linked together into a master assembly. (You will need to open in Fusion 360 directly to see the history, since the web version does not show that.)

## Design Guidelines

* All parts should match the Voron original parts as closely as possible.
  However, very small details that do not affect functionality do not need to be
  perfectly reconstructed. Examples:
  * If a complex shape could be constructed from a loft, an extruded cut,
    or a combination of fillets, please use whichever is most expedient.
    It's not necessary to choose the one which most exactly matches the
    result achieved in the original part.
  * Fillets and chamfers should have the same radius as the original
    part, but only within 0.05mm.
* Including Voron logos and branding is optional, but preferred. All text should
  remain editable - no vector text please. The Voron logo is available in
  parametric F3D and rendered vector SVG formats in the [assets](assets) folder.
  The font used for branding is
  [Play](https://fonts.google.com/specimen/Play?preview.text=VORON&preview.text_type=custom)
  from Google Fonts.
* User parameters should be used where possible, for anything the user
  is very likely to want to change (e.g. the length of an extrude for
  something like a panel thickness), or for values which are reused frequently
  within the design and might need to be changed. However: a working part
  with no user parameters is preferable to no working part at all!
  Feel free to open a PR even if your F3D doesn't use them.
* A pair of parts that are mirror images of each other only needs to have one
  F3D file uploaded, to avoid duplication. It is the user's responsibility
  to flip the part as needed before printing in the slicer.
* Use millimeter measurements throughout.

## Standard Parameter Names

For consistency across parts, where possible, please use the following names
for various standard parameters (all units are millimeters):

| Parameter Name | Definition |
| --- | --- |
| chamfer | Default chamfer, typically 0.4mm |
| extrusion_width | Extrusion width |
| panel_thickness | Panel thickness, including foam tape and VHB as needed |
| rail_width | Linear rail width |
| tolerance | Tolerance added for good fit, typically 0.2mm |
| z_belt_distance | Distance between the Z belts |
| z_belt_width | Width of the Z belts |

## Design Tips

An easy way to reconstruct a part is to import the original piece from the
official Voron F3D CAD, center it, then start drawing sketches around it to
capture the main dimensions. As you build up the part, you can hide or show the
original body to compare against your component, and see what else you need to do.

To do this:

* Open the original CAD F3D file in Fusion 360.
* Find the part you are interested in in the heirarchy view.
* Right click, and select "Save Copy As".
* Open the new part and make it editable. Click on the body, go to
  MODIFY -> Align, and select the origin.

Before starting work, you MUST do the following, otherwise you will find
yourself having to start all over again:

* Turn on design history: right click the top level item in the heirarchy,
  and select "Capture Design History."
* Create a new component: ASSEMBLE -> New Component.
* Name the component to match the name of the part.
* Activate the component in the heirarchy.
* When starting your first sketch, be sure to select a plane that is
  part of the new component, and not a face of the imported body.
  Hiding the imported body temporarily is a good way to ensure this.

While working, you can capture measurements like distances, XYZ coordinates,
and radii, by selecting appropriate points, lines, and curves, in the original
component, and by using the INSPECT -> Measure tool as needed.

Don't forget to save your work often, since Fusion 360 can be unstable when
used with certain graphics drivers. If you have an Nvidia graphics card
and are running Windows, switch to the Studio driver using Geforce Experience
(use the three dots icon at the top right of the DRIVERS tab), it is much
more stable.

Before exporting, you can delete the imported body from the heirarchy.

Always follow the two golden rules of Fusion 360:

1. Before doing anything, create a component and make sure it's activated.
2. Name your components, sketches, and so on.

It's important to be aware of some shortcomings of Fusion 360 that require
workarounds:

* Extrudes in "join" mode combine bodies based on what is visible in the
  viewport at the time the designer does the join. However, this information
  is not captured in the design history! If you go back and edit the extrude,
  or modify a user parameter, Fusion may recombine bodies in a way that
  breaks the rest of the timeline. The solution is to put bodies that
  should stay separate into separate components: extrude will not join bodies
  from different components.

## License

All parts are licensed under the GPLv3. For the purposes of the GPL license:

- "Source code" means:
  - Original parametric Fusion 360 (F3D) files, with design history enabled, fully visible, and editable.
  - Similar files from Autodesk Inventor, Solidworks, and any other parametric CAD tool.
  - DXFs and other editable vector-based graphics files.
  - Bitmap image files such as PNGs and JPGs.
  - Any other files which would normally be considered "source code" in a software project covered by GPLv3, such as scripts and source code in any programming language.
- "Object code" means:
  - STEP files, STL files, 3MF files, F3D or other parametric CAD files which have had design history or original sketches removed or disabled.
  - Any bit sequence compiled from the "source code" or any derivative thereof, into a form from which the original "source code" cannot be directly retrieved.

Unless otherwise specified, copyright for each F3D file is owned collectively by the individual who committed (or is listed as an author in the commit for) the initial version of the file, and any individual who committed (or is listed as an author in the commit for) any modifications to it.