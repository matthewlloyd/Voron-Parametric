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
| ab_belt_width | Width of the AB belts |
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

## Progress (as of 2021-09-03)

### Voron-2 (32/131, 24%)

- :black_large_square: TEST_PRINTS (0/3, 0%)
  - :black_large_square: Filament Card Caddy 25.stl
  - :black_large_square: Filament Card.stl
  - :black_large_square: Voron_Design_Cube_v7.stl
- :black_large_square: VORON2.4 (32/128, 25%)
  - :black_large_square: Electronics_Compartment (0/15, 0%)
    - :black_large_square: DIN_Brackets (0/8, 0%)
      - :black_large_square: duet_duex_bracket_x2.stl
      - :black_large_square: lrs_psu_bracket_clip.stl
      - :black_large_square: pcb_din_clip_x3.stl
      - :black_large_square: ramps_bracket_x2.stl
      - :black_large_square: raspberrypi_bracket.stl
      - :black_large_square: rs25_psu_bracket_clip.stl
      - :black_large_square: skr_1.3_1.4_bracket_x2.stl
      - :black_large_square: skr_mini_e3_bracket_x2.stl
    - :black_large_square: LCD_Module (0/4, 0%)
      - :black_large_square: [a]_mini12864_case_hinge.stl
      - :black_large_square: mini12864_case_front.stl
      - :black_large_square: mini12864_case_rear.stl
      - :black_large_square: mini12864_spacer.stl
    - :black_large_square: Plug_Panel (0/3, 0%)
      - :black_large_square: [a]_keystone_blank_insert.stl
      - :black_large_square: plug_panel.stl
      - :black_large_square: plug_panel_filtered_mains.stl
  - :black_large_square: Exhaust_Filter (2/4, 50%)
    - :white_check_mark: [a]_exhaust_filter_mount_x2.stl
    - :black_large_square: [a]_filter_access_cover.stl
    - :white_check_mark: exhaust_filter_grill.stl
    - :black_large_square: exhaust_filter_housing.stl
  - :black_large_square: Gantry (11/54, 20%)
    - :white_check_mark: [a]_z_belt_clip_lower_x4.stl
    - :white_check_mark: [a]_z_belt_clip_upper_x4.stl
    - :black_large_square: z_chain_bottom_anchor.stl
    - :black_large_square: z_chain_guide.stl
    - :black_large_square: AB_Drive_Units (1/6, 17%)
      - :black_large_square: [a]_cable_cover.stl
      - :white_check_mark: [a]_z_chain_retainer_bracket_x2.stl
      - :black_large_square: a_drive_frame_lower.stl
      - :black_large_square: a_drive_frame_upper.stl
      - :black_large_square: b_drive_frame_lower.stl
      - :black_large_square: b_drive_frame_upper.stl
    - :black_large_square: Front_Idlers (2/6, 33%)
      - :white_check_mark: [a]_tensioner_left.stl
      - :white_check_mark: [a]_tensioner_right.stl
      - :black_large_square: front_idler_left_lower.stl
      - :black_large_square: front_idler_left_upper.stl
      - :black_large_square: front_idler_right_lower.stl
      - :black_large_square: front_idler_right_upper.stl
    - :black_large_square: X_Axis (5/35, 14%)
      - :black_large_square: XY_Joints (0/8, 0%)
        - :black_large_square: [a]_endstop_pod_hall_effect.stl
        - :black_large_square: [a]_endstop_pod_microswitch.stl
        - :black_large_square: [a]_xy_joint_cable_bridge_generic.stl
        - :black_large_square: [a]_xy_joint_cable_bridge_igus.stl
        - :black_large_square: xy_joint_left_lower.stl
        - :black_large_square: xy_joint_left_upper.stl
        - :black_large_square: xy_joint_right_lower.stl
        - :black_large_square: xy_joint_right_upper.stl
      - :black_large_square: X_Carriage (5/27, 19%)
        - :white_check_mark: [a]_belt_clamp_x2.stl
        - :black_large_square: [a]_blower_housing_front.stl
        - :black_large_square: blower_housing_rear.stl
        - :black_large_square: hotend_fan_mount.stl
        - :white_check_mark: probe_retainer_bracket.stl
        - :black_large_square: x_carriage_frame_left.stl
        - :black_large_square: x_carriage_frame_right.stl
        - :white_check_mark: x_carriage_pivot_block.stl
        - :black_large_square: Bowden (0/5, 0%)
          - :black_large_square: bowden_module_front.stl
          - :black_large_square: bowden_module_rear_generic.stl
          - :black_large_square: bowden_module_rear_igus.stl
          - :black_large_square: bsp_adapter.stl
          - :black_large_square: tl_collet_adapter.stl
        - :black_large_square: Direct_Feed (2/8, 25%)
          - :black_large_square: [a]_connector_cover.stl
          - :black_large_square: [a]_guidler.stl
          - :white_check_mark: [a]_latch.stl
          - :black_large_square: chain_anchor_generic.stl
          - :black_large_square: chain_anchor_igus.stl
          - :black_large_square: extruder_body.stl
          - :black_large_square: extruder_motor_plate.stl
          - :white_check_mark: latch_shuttle.stl
        - :black_large_square: Printheads (0/6, 0%)
          - :black_large_square: E3D_V6 (0/2, 0%)
            - :black_large_square: printhead_front_e3dv6.stl
            - :black_large_square: printhead_rear_e3dv6.stl
          - :black_large_square: Slice_Mosquito (0/2, 0%)
            - :black_large_square: printhead_front_mosquito.stl
            - :black_large_square: printhead_rear_mosquito.stl
          - :black_large_square: TriangleLab_Dragon (0/2, 0%)
            - :black_large_square: printhead_front_dragon.stl
            - :black_large_square: printhead_rear_dragon.stl
    - :black_large_square: Z_Joints (1/3, 33%)
      - :black_large_square: z_joint_lower_x4.stl
      - :black_large_square: z_joint_upper_hall_effect.stl
      - :white_check_mark: z_joint_upper_x4.stl
  - :black_large_square: Panel_Mounting (10/12, 83%)
    - :black_large_square: bottom_panel_clip_x4.stl
    - :black_large_square: bottom_panel_hinge_x2.stl
    - :white_check_mark: corner_panel_clip_3mm_x12.stl
    - :white_check_mark: corner_panel_clip_6mm_x4.stl
    - :white_check_mark: midspan_panel_clip_3mm_x12.stl
    - :white_check_mark: midspan_panel_clip_6mm_x3.stl
    - :white_check_mark: z_belt_cover_a_x2.stl
    - :white_check_mark: z_belt_cover_b_x2.stl
    - :white_check_mark: Front_Doors (4/4, 100%)
      - :white_check_mark: door_hinge_x4.stl
      - :white_check_mark: handle_a_x2.stl
      - :white_check_mark: handle_b_x2.stl
      - :white_check_mark: latch_x2.stl
  - :black_large_square: Skirts (1/16, 6%)
    - :white_check_mark: [a]_60mm_fan_blank_insert_x2.stl
    - :black_large_square: [a]_belt_guard_a_x2.stl
    - :black_large_square: [a]_belt_guard_b_x2.stl
    - :black_large_square: side_fan_support_x2.stl
    - :black_large_square: 250 (0/4, 0%)
      - :black_large_square: front_rear_skirt_a_250_x2.stl
      - :black_large_square: front_rear_skirt_b_250_x2.stl
      - :black_large_square: side_skirt_a_250_x2.stl
      - :black_large_square: side_skirt_b_250_x2.stl
    - :black_large_square: 300 (0/4, 0%)
      - :black_large_square: front_rear_skirt_a_300_x2.stl
      - :black_large_square: front_rear_skirt_b_300_x2.stl
      - :black_large_square: side_skirt_a_300_x2.stl
      - :black_large_square: side_skirt_b_300_x2.stl
    - :black_large_square: 350 (0/4, 0%)
      - :black_large_square: front_rear_skirt_a_350_x2.stl
      - :black_large_square: front_rear_skirt_b_350_x2.stl
      - :black_large_square: side_skirt_a_350_x2.stl
      - :black_large_square: side_skirt_b_350_x2.stl
  - :black_large_square: Spool_Management (0/2, 0%)
    - :black_large_square: bowen_retainer.stl
    - :black_large_square: spool_holder.stl
  - :black_large_square: Tools (1/2, 50%)
    - :black_large_square: bed_hole_marking_template_x1_Rev2.stl
    - :white_check_mark: rail_installation_guide_center_x2.stl
  - :black_large_square: Z_Drive (2/11, 18%)
    - :black_large_square: [a]_belt_tensioner_a_x2.stl
    - :black_large_square: [a]_belt_tensioner_b_x2.stl
    - :black_large_square: [a]_stopgap_80T_hubbed_gear.stl
    - :white_check_mark: [a]_z_drive_baseplate_a_x2.stl
    - :white_check_mark: [a]_z_drive_baseplate_b_x2.stl
    - :black_large_square: z_drive_main_a_x2.stl
    - :black_large_square: z_drive_main_b_x2.stl
    - :black_large_square: z_drive_retainer_a_x2.stl
    - :black_large_square: z_drive_retainer_b_x2.stl
    - :black_large_square: z_motor_mount_a_x2.stl
    - :black_large_square: z_motor_mount_b_x2.stl
  - :white_check_mark: Z_Endstop (1/1, 100%)
    - :white_check_mark: nozzle_probe.stl
  - :white_check_mark: Z_Idlers (4/4, 100%)
    - :white_check_mark: [a]_z_tensioner_x4_6mm.stl
    - :white_check_mark: [a]_z_tensioner_x4_9mm.stl
    - :white_check_mark: z_tensioner_bracket_a_x2.stl
    - :white_check_mark: z_tensioner_bracket_b_x2.stl
  - :black_large_square: ZipChain (0/7, 0%)
    - :black_large_square: XY (0/3, 0%)
      - :black_large_square: zipchain2_xy_end.stl
      - :black_large_square: zipchain2_xy_link_a.stl
      - :black_large_square: zipchain2_xy_link_b.stl
    - :black_large_square: Z (0/4, 0%)
      - :black_large_square: zipchain2_z_end.stl
      - :black_large_square: zipchain2_z_link_a.stl
      - :black_large_square: zipchain2_z_link_b.stl
      - :black_large_square: zipchain2_z_link_b_locking.stl

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
