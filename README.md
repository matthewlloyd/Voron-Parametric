# The Parametric Voron

This repository contains Fusion 360 reconstructions of various printed parts from the Voron printers (https://vorondesign.com/). Unlike the CAD files provided by the Voron team, these files have full parametric design history turned on, and are easy to edit.

This is a community effort and it may take months, or even years, to recreate the full set of parts. If you would like to contribute, feel free to open a pull request. Parts are organized per Voron release, with the same directory structure and naming conventions used by the original Voron parts.

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
  remain editable - no vector text please.
* User parameters should be used where possible, for anything the user
  is very likely to want to change (e.g. the length of an extrude for
  something like a panel thickness), or for values which are reused frequently
  within the design and might need to be changed. However: a working part
  with no user parameters is preferable to no working part at all!
  Feel free to open a PR even if your F3D doesn't use them.
* A pair of parts that are mirror images of each other only needs to have one
  F3D file uploaded, to avoid duplication. It is the user's responsibility
  to flip the part as needed before printing in the slicer.

## Design Tips

An easy way to reconstruct a part is to import the original STL as a mesh,
center it, then start drawing sketches around it to capture the main
dimensions. As you build up the part, you can hide or show the mesh
to compare against your component, and see what else you need to do.

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