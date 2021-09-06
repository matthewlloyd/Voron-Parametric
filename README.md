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

<!-- BEGIN_STATS generated by scripts/stats.py, do not edit -->
# Progress (as of 2021-09-06 13:35 EDT)

## Voron-2
<img src="https://progress-bar.dev/35?width=500&title_width=50&title=%2046%2f131"/>

<details markdown="1"><summary markdown="1">Click to expand file tree...</summary>

- :black_large_square: TEST_PRINTS (1/3, 33%)
  - :black_large_square: Filament Card Caddy 25
  - :black_large_square: Filament Card
  - :white_check_mark: [Voron_Design_Cube_v7](./Voron-2/TEST_PRINTS/Voron_Design_Cube_v7.f3d)
- :black_large_square: VORON2.4 (45/128, 35%)
  - :black_large_square: Electronics_Compartment (2/15, 13%)
    - :black_large_square: DIN_Brackets (2/8, 25%)
      - :black_large_square: duet_duex_bracket_x2
      - :black_large_square: lrs_psu_bracket_clip
      - :white_check_mark: [pcb_din_clip_x3](./Voron-2/VORON2.4/Electronics_Compartment/DIN_Brackets/pcb_din_clip_x3.f3d)
      - :black_large_square: ramps_bracket_x2
      - :black_large_square: raspberrypi_bracket
      - :black_large_square: rs25_psu_bracket_clip
      - :white_check_mark: [skr_1.3_1.4_bracket_x2](./Voron-2/VORON2.4/Electronics_Compartment/DIN_Brackets/skr_1.3_1.4_bracket_x2.f3d)
      - :black_large_square: skr_mini_e3_bracket_x2
    - :black_large_square: LCD_Module (0/4, 0%)
      - :black_large_square: [a]_mini12864_case_hinge
      - :black_large_square: mini12864_case_front
      - :black_large_square: mini12864_case_rear
      - :black_large_square: mini12864_spacer
    - :black_large_square: Plug_Panel (0/3, 0%)
      - :black_large_square: [a]_keystone_blank_insert
      - :black_large_square: plug_panel
      - :black_large_square: plug_panel_filtered_mains
  - :black_large_square: Exhaust_Filter (2/4, 50%)
    - :white_check_mark: [[a]_exhaust_filter_mount_x2](./Voron-2/VORON2.4/Exhaust_Filter/[a]_exhaust_filter_mount_x2.f3d)
    - :black_large_square: [a]_filter_access_cover
    - :white_check_mark: [exhaust_filter_grill](./Voron-2/VORON2.4/Exhaust_Filter/exhaust_filter_grill.f3d)
    - :black_large_square: exhaust_filter_housing
  - :black_large_square: Gantry (15/54, 28%)
    - :white_check_mark: [[a]_z_belt_clip_lower_x4](./Voron-2/VORON2.4/Gantry/[a]_z_belt_clip_lower_x4.f3d)
    - :white_check_mark: [[a]_z_belt_clip_upper_x4](./Voron-2/VORON2.4/Gantry/[a]_z_belt_clip_upper_x4.f3d)
    - :black_large_square: z_chain_bottom_anchor
    - :black_large_square: z_chain_guide
    - :black_large_square: AB_Drive_Units (1/6, 17%)
      - :black_large_square: [a]_cable_cover
      - :white_check_mark: [[a]_z_chain_retainer_bracket_x2](./Voron-2/VORON2.4/Gantry/AB_Drive_Units/[a]_z_chain_retainer_bracket_x2.f3d)
      - :black_large_square: a_drive_frame_lower
      - :black_large_square: a_drive_frame_upper
      - :black_large_square: b_drive_frame_lower
      - :black_large_square: b_drive_frame_upper
    - :black_large_square: Front_Idlers (2/6, 33%)
      - :white_check_mark: [[a]_tensioner_left](./Voron-2/VORON2.4/Gantry/Front_Idlers/[a]_tensioner_left.f3d)
      - :white_check_mark: [[a]_tensioner_right](./Voron-2/VORON2.4/Gantry/Front_Idlers/[a]_tensioner_left.f3d)
      - :black_large_square: front_idler_left_lower
      - :black_large_square: front_idler_left_upper
      - :black_large_square: front_idler_right_lower
      - :black_large_square: front_idler_right_upper
    - :black_large_square: X_Axis (7/35, 20%)
      - :black_large_square: XY_Joints (0/8, 0%)
        - :black_large_square: [a]_endstop_pod_hall_effect
        - :black_large_square: [a]_endstop_pod_microswitch
        - :black_large_square: [a]_xy_joint_cable_bridge_generic
        - :black_large_square: [a]_xy_joint_cable_bridge_igus
        - :black_large_square: xy_joint_left_lower
        - :black_large_square: xy_joint_left_upper
        - :black_large_square: xy_joint_right_lower
        - :black_large_square: xy_joint_right_upper
      - :black_large_square: X_Carriage (7/27, 26%)
        - :white_check_mark: [[a]_belt_clamp_x2](./Voron-2/VORON2.4/Gantry/X_Axis/X_Carriage/[a]_belt_clamp_x2.f3d)
        - :black_large_square: [a]_blower_housing_front
        - :black_large_square: blower_housing_rear
        - :black_large_square: hotend_fan_mount
        - :white_check_mark: [probe_retainer_bracket](./Voron-2/VORON2.4/Gantry/X_Axis/X_Carriage/probe_retainer_bracket.f3d)
        - :black_large_square: x_carriage_frame_left
        - :black_large_square: x_carriage_frame_right
        - :white_check_mark: [x_carriage_pivot_block](./Voron-2/VORON2.4/Gantry/X_Axis/X_Carriage/x_carriage_pivot_block.f3d)
        - :black_large_square: Bowden (0/5, 0%)
          - :black_large_square: bowden_module_front
          - :black_large_square: bowden_module_rear_generic
          - :black_large_square: bowden_module_rear_igus
          - :black_large_square: bsp_adapter
          - :black_large_square: tl_collet_adapter
        - :black_large_square: Direct_Feed (4/8, 50%)
          - :black_large_square: [a]_connector_cover
          - :black_large_square: [a]_guidler
          - :white_check_mark: [[a]_latch](./Voron-2/VORON2.4/Gantry/X_Axis/X_Carriage/Direct_Feed/[a]_latch.f3d)
          - :white_check_mark: [chain_anchor_generic](./Voron-2/VORON2.4/Gantry/X_Axis/X_Carriage/Direct_Feed/chain_anchor_generic.f3d)
          - :white_check_mark: [chain_anchor_igus](./Voron-2/VORON2.4/Gantry/X_Axis/X_Carriage/Direct_Feed/chain_anchor_igus.f3d)
          - :black_large_square: extruder_body
          - :black_large_square: extruder_motor_plate
          - :white_check_mark: [latch_shuttle](./Voron-2/VORON2.4/Gantry/X_Axis/X_Carriage/Direct_Feed/latch_shuttle.f3d)
        - :black_large_square: Printheads (0/6, 0%)
          - :black_large_square: E3D_V6 (0/2, 0%)
            - :black_large_square: printhead_front_e3dv6
            - :black_large_square: printhead_rear_e3dv6
          - :black_large_square: Slice_Mosquito (0/2, 0%)
            - :black_large_square: printhead_front_mosquito
            - :black_large_square: printhead_rear_mosquito
          - :black_large_square: TriangleLab_Dragon (0/2, 0%)
            - :black_large_square: printhead_front_dragon
            - :black_large_square: printhead_rear_dragon
    - :white_check_mark: Z_Joints (3/3, 100%)
      - :white_check_mark: [z_joint_lower_x4](./Voron-2/VORON2.4/Gantry/Z_Joints/z_joint_lower_x4.f3d)
      - :white_check_mark: [z_joint_upper_hall_effect](./Voron-2/VORON2.4/Gantry/Z_Joints/z_joint_upper_hall_effect.f3d)
      - :white_check_mark: [z_joint_upper_x4](./Voron-2/VORON2.4/Gantry/Z_Joints/z_joint_upper_x4.f3d)
  - :black_large_square: Panel_Mounting (10/12, 83%)
    - :black_large_square: bottom_panel_clip_x4
    - :black_large_square: bottom_panel_hinge_x2
    - :white_check_mark: [corner_panel_clip_3mm_x12](./Voron-2/VORON2.4/Panel_Mounting/corner_panel_clip_3mm_x12.f3d)
    - :white_check_mark: [corner_panel_clip_6mm_x4](./Voron-2/VORON2.4/Panel_Mounting/corner_panel_clip_3mm_x12.f3d)
    - :white_check_mark: [midspan_panel_clip_3mm_x12](./Voron-2/VORON2.4/Panel_Mounting/midspan_panel_clip_3mm_x12.f3d)
    - :white_check_mark: [midspan_panel_clip_6mm_x3](./Voron-2/VORON2.4/Panel_Mounting/midspan_panel_clip_3mm_x12.f3d)
    - :white_check_mark: [z_belt_cover_a_x2](./Voron-2/VORON2.4/Panel_Mounting/z_belt_cover_a_x2.f3d)
    - :white_check_mark: [z_belt_cover_b_x2](./Voron-2/VORON2.4/Panel_Mounting/z_belt_cover_a_x2.f3d)
    - :white_check_mark: Front_Doors (4/4, 100%)
      - :white_check_mark: [door_hinge_x4](./Voron-2/VORON2.4/Panel_Mounting/Front_Doors/door_hinge_x4.f3d)
      - :white_check_mark: [handle_a_x2](./Voron-2/VORON2.4/Panel_Mounting/Front_Doors/handle_a_x2.f3d)
      - :white_check_mark: [handle_b_x2](./Voron-2/VORON2.4/Panel_Mounting/Front_Doors/handle_a_x2.f3d)
      - :white_check_mark: [latch_x2](./Voron-2/VORON2.4/Panel_Mounting/Front_Doors/latch_x2.f3d)
  - :black_large_square: Skirts (1/16, 6%)
    - :white_check_mark: [[a]_60mm_fan_blank_insert_x2](./Voron-2/VORON2.4/Skirts/[a]_60mm_fan_blank_insert_x2.f3d)
    - :black_large_square: [a]_belt_guard_a_x2
    - :black_large_square: [a]_belt_guard_b_x2
    - :black_large_square: side_fan_support_x2
    - :black_large_square: 250 (0/4, 0%)
      - :black_large_square: front_rear_skirt_a_250_x2
      - :black_large_square: front_rear_skirt_b_250_x2
      - :black_large_square: side_skirt_a_250_x2
      - :black_large_square: side_skirt_b_250_x2
    - :black_large_square: 300 (0/4, 0%)
      - :black_large_square: front_rear_skirt_a_300_x2
      - :black_large_square: front_rear_skirt_b_300_x2
      - :black_large_square: side_skirt_a_300_x2
      - :black_large_square: side_skirt_b_300_x2
    - :black_large_square: 350 (0/4, 0%)
      - :black_large_square: front_rear_skirt_a_350_x2
      - :black_large_square: front_rear_skirt_b_350_x2
      - :black_large_square: side_skirt_a_350_x2
      - :black_large_square: side_skirt_b_350_x2
  - :white_check_mark: Spool_Management (2/2, 100%)
    - :white_check_mark: [bowen_retainer](./Voron-2/VORON2.4/Spool_Management/bowen_retainer.f3d)
    - :white_check_mark: [spool_holder](./Voron-2/VORON2.4/Spool_Management/spool_holder.f3d)
  - :white_check_mark: Tools (2/2, 100%)
    - :white_check_mark: [bed_hole_marking_template_x1_Rev2](./Voron-2/VORON2.4/Tools/bed_hole_marking_template_x1_Rev2.f3d)
    - :white_check_mark: [rail_installation_guide_center_x2](./Voron-2/VORON2.4/Tools/rail_installation_guide_center_x2.f3d)
  - :black_large_square: Z_Drive (6/11, 55%)
    - :white_check_mark: [[a]_belt_tensioner_a_x2](./Voron-2/VORON2.4/Z_Drive/[a]_belt_tensioner_a_x2.f3d)
    - :white_check_mark: [[a]_belt_tensioner_b_x2](./Voron-2/VORON2.4/Z_Drive/[a]_belt_tensioner_a_x2.f3d)
    - :black_large_square: [a]_stopgap_80T_hubbed_gear
    - :white_check_mark: [[a]_z_drive_baseplate_a_x2](./Voron-2/VORON2.4/Z_Drive/[a]_z_drive_baseplate_a_x2.f3d)
    - :white_check_mark: [[a]_z_drive_baseplate_b_x2](./Voron-2/VORON2.4/Z_Drive/[a]_z_drive_baseplate_a_x2.f3d)
    - :black_large_square: z_drive_main_a_x2
    - :black_large_square: z_drive_main_b_x2
    - :black_large_square: z_drive_retainer_a_x2
    - :black_large_square: z_drive_retainer_b_x2
    - :white_check_mark: [z_motor_mount_a_x2](./Voron-2/VORON2.4/Z_Drive/z_motor_mount_a_x2.f3d)
    - :white_check_mark: [z_motor_mount_b_x2](./Voron-2/VORON2.4/Z_Drive/z_motor_mount_a_x2.f3d)
  - :white_check_mark: Z_Endstop (1/1, 100%)
    - :white_check_mark: [nozzle_probe](./Voron-2/VORON2.4/Z_Endstop/nozzle_probe.f3d)
  - :white_check_mark: Z_Idlers (4/4, 100%)
    - :white_check_mark: [[a]_z_tensioner_x4_6mm](./Voron-2/VORON2.4/Z_Idlers/[a]_z_tensioner_x4_6mm.f3d)
    - :white_check_mark: [[a]_z_tensioner_x4_9mm](./Voron-2/VORON2.4/Z_Idlers/[a]_z_tensioner_x4_6mm.f3d)
    - :white_check_mark: [z_tensioner_bracket_a_x2](./Voron-2/VORON2.4/Z_Idlers/z_tensioner_bracket_a_x2.f3d)
    - :white_check_mark: [z_tensioner_bracket_b_x2](./Voron-2/VORON2.4/Z_Idlers/z_tensioner_bracket_a_x2.f3d)
  - :black_large_square: ZipChain (0/7, 0%)
    - :black_large_square: XY (0/3, 0%)
      - :black_large_square: zipchain2_xy_end
      - :black_large_square: zipchain2_xy_link_a
      - :black_large_square: zipchain2_xy_link_b
    - :black_large_square: Z (0/4, 0%)
      - :black_large_square: zipchain2_z_end
      - :black_large_square: zipchain2_z_link_a
      - :black_large_square: zipchain2_z_link_b
      - :black_large_square: zipchain2_z_link_b_locking
</details>

## Voron-Trident
<img src="https://progress-bar.dev/0?width=500&title_width=50&title=%20%200%2f140"/>

<details markdown="1"><summary markdown="1">Click to expand file tree...</summary>

- :black_large_square: ElectronicsBay (0/17, 0%)
  - :black_large_square: DIN_center_support_x2
  - :black_large_square: DIN_frame_mount_x4
  - :black_large_square: PSU_stabilizer_50mm
  - :black_large_square: cable_frame_anchor_x6
  - :black_large_square: lrs_psu_bracket_x2
  - :black_large_square: pcb_din_clip_v2_x5
  - :black_large_square: raspberrypi_bracket
  - :black_large_square: rs25_psu_bracket
  - :black_large_square: Controller_Mounts (0/7, 0%)
    - :black_large_square: BTT_MOT_EXP_bracket
    - :black_large_square: Duet2_Duet3Mini5_bracket_2pc
    - :black_large_square: GTR_bracket_2pc
    - :black_large_square: Octopus_bracket_2pc
    - :black_large_square: SKR_Pro_bracket_2pc
    - :black_large_square: SKR_bracket_inline_2pc
    - :black_large_square: Spider_bracket_2pc
  - :black_large_square: Other_PS_Mounts (0/2, 0%)
    - :black_large_square: UHP_200_Mount_x2
    - :black_large_square: UHP_350_Mount_x2
- :black_large_square: Exhaust_Filter (0/4, 0%)
  - :black_large_square: [a]_exhaust_filter_mount_x2
  - :black_large_square: [a]_filter_access_cover
  - :black_large_square: exhaust_filter_grill
  - :black_large_square: exhaust_filter_housing
- :black_large_square: Gantry (0/49, 0%)
  - :black_large_square: AB_Drive_Units (0/7, 0%)
    - :black_large_square: [a]_wire_cover
    - :black_large_square: [a]_y_endstop_bumper
    - :black_large_square: [a]_y_endstop_housing
    - :black_large_square: a_drive_frame_lower
    - :black_large_square: a_drive_frame_upper
    - :black_large_square: b_drive_frame_lower
    - :black_large_square: b_drive_frame_upper
  - :black_large_square: Front_Idlers (0/4, 0%)
    - :black_large_square: [a]_tensioner_left
    - :black_large_square: [a]_tensioner_right
    - :black_large_square: front_idler_a_x2
    - :black_large_square: front_idler_b_x2
  - :black_large_square: X_Axis (0/38, 0%)
    - :black_large_square: XY_Joints (0/8, 0%)
      - :black_large_square: [a]_endstop_pod_hall_effect
      - :black_large_square: [a]_endstop_pod_microswitch
      - :black_large_square: [a]_xy_joint_cable_bridge_2hole
      - :black_large_square: [a]_xy_joint_cable_bridge_3hole
      - :black_large_square: xy_joint_left_lower_MGN12
      - :black_large_square: xy_joint_left_upper_MGN12
      - :black_large_square: xy_joint_right_lower_MGN12
      - :black_large_square: xy_joint_right_upper_MGN12
    - :black_large_square: X_Carriage (0/30, 0%)
      - :black_large_square: [a]_blower_housing_front
      - :black_large_square: blower_housing_rear
      - :black_large_square: hotend_fan_mount
      - :black_large_square: probe_retainer_bracket
      - :black_large_square: probe_retainer_bracket_9mm
      - :black_large_square: x_carriage_frame_left
      - :black_large_square: x_carriage_frame_right
      - :black_large_square: Bowden (0/5, 0%)
        - :black_large_square: bowden_module_front
        - :black_large_square: bowden_module_rear_10x11chains
        - :black_large_square: bowden_module_rear_igus
        - :black_large_square: bsp_adapter
        - :black_large_square: tl_collet_adapter
      - :black_large_square: Direct Feed (0/8, 0%)
        - :black_large_square: [a]_connector_cover
        - :black_large_square: [a]_guidler
        - :black_large_square: [a]_latch
        - :black_large_square: [a]_latch_shuttle
        - :black_large_square: chain_anchor_2hole
        - :black_large_square: chain_anchor_3hole
        - :black_large_square: extruder_body
        - :black_large_square: extruder_motor_plate
      - :black_large_square: Toolheads (0/10, 0%)
        - :black_large_square: Dragon (0/2, 0%)
          - :black_large_square: printhead_front_dragon
          - :black_large_square: printhead_rear_dragon
        - :black_large_square: Dragonfly_BMO (0/2, 0%)
          - :black_large_square: printhead_front_dragonfly_bmo
          - :black_large_square: printhead_rear_dragonfly_bmo
        - :black_large_square: Dragonfly_BMS (0/2, 0%)
          - :black_large_square: printhead_front_dragonfly_bms
          - :black_large_square: printhead_rear_dragonfly_bms
        - :black_large_square: E3D V6 (0/2, 0%)
          - :black_large_square: printhead_front_e3dv6
          - :black_large_square: printhead_rear_e3dv6
        - :black_large_square: Slice Mosquito (0/2, 0%)
          - :black_large_square: printhead_front_mosquito
          - :black_large_square: printhead_rear_mosquito
- :black_large_square: Panels (0/14, 0%)
  - :black_large_square: bottom_panel_clip_x4
  - :black_large_square: bottom_panel_hinge_x2
  - :black_large_square: corner_panel_clip_4mm_x8
  - :black_large_square: corner_panel_clip_6mm_x8
  - :black_large_square: deck_support_3mm_x8
  - :black_large_square: deck_support_4mm_x8
  - :black_large_square: midspan_panel_clip_4mm_x7
  - :black_large_square: midspan_panel_clip_6mm_x8
  - :black_large_square: wire_corner_left
  - :black_large_square: wire_corner_right
  - :black_large_square: Front_Doors (0/4, 0%)
    - :black_large_square: door_hinge_x6
    - :black_large_square: handle_a_x2
    - :black_large_square: handle_b_x2
    - :black_large_square: latch_x2
- :black_large_square: Skirt (0/30, 0%)
  - :black_large_square: [a]_60mm_fan_blank_insert_x2
  - :black_large_square: [a]_corner_baseplate_a_x2
  - :black_large_square: [a]_corner_baseplate_b_x2
  - :black_large_square: [a]_keystone_blank_insert_x2
  - :black_large_square: [a]_mini12864_case_front_insert
  - :black_large_square: [a]_mini12864_case_hinge
  - :black_large_square: [a]_skirt_logo_x2
  - :black_large_square: corner_a_x2
  - :black_large_square: corner_b_x2
  - :black_large_square: keystone_panel
  - :black_large_square: mini12864_case_front
  - :black_large_square: mini12864_case_rear
  - :black_large_square: power_inlet_adamstech
  - :black_large_square: power_inlet_filtered
  - :black_large_square: side_fan_support_x2
  - :black_large_square: 250 (0/5, 0%)
    - :black_large_square: front_skirt_a_250
    - :black_large_square: front_skirt_b_250
    - :black_large_square: rear_center_skirt_250
    - :black_large_square: side_skirt_a_250_x2
    - :black_large_square: side_skirt_b_250_x2
  - :black_large_square: 300 (0/5, 0%)
    - :black_large_square: front_skirt_a_300
    - :black_large_square: front_skirt_b_300
    - :black_large_square: rear_center_skirt_300
    - :black_large_square: side_skirt_a_300_x2
    - :black_large_square: side_skirt_b_300_x2
  - :black_large_square: 350 (0/5, 0%)
    - :black_large_square: front_skirt_a_350
    - :black_large_square: front_skirt_b_350
    - :black_large_square: rear_center_skirt_350
    - :black_large_square: side_skirt_a_350_x2
    - :black_large_square: side_skirt_b_350_x2
- :black_large_square: Spool_Management (0/2, 0%)
  - :black_large_square: bowen_retainer
  - :black_large_square: spool_holder
- :black_large_square: Tools (0/6, 0%)
  - :black_large_square: 10mm_extrusion_drill_guide
  - :black_large_square: 110mm_Y_alignment_spacer_x2
  - :black_large_square: 140mm_extrusion_drill_guide
  - :black_large_square: AB_pulley_jig
  - :black_large_square: MGN12_rail_guide_x2
  - :black_large_square: MGN9_rail_guide_x2
- :black_large_square: Z_Assembly (0/18, 0%)
  - :black_large_square: [a]_z_carriage_left
  - :black_large_square: [a]_z_carriage_right
  - :black_large_square: [a]_z_rail_stop_x3
  - :black_large_square: nozzle_probe
  - :black_large_square: z_bed_left
  - :black_large_square: z_bed_rear
  - :black_large_square: z_bed_right
  - :black_large_square: z_cable_chain_mount_2hole
  - :black_large_square: z_cable_chain_mount_3hole
  - :black_large_square: z_carriage_left
  - :black_large_square: z_carriage_rear_2hole
  - :black_large_square: z_carriage_rear_3hole
  - :black_large_square: z_carriage_right
  - :black_large_square: z_rear_extrusionbracket_left
  - :black_large_square: z_rear_extrusionbracket_right
  - :black_large_square: z_stepper_left
  - :black_large_square: z_stepper_rear
  - :black_large_square: z_stepper_right
</details>

## Voron-0
<img src="https://progress-bar.dev/0?width=500&title_width=50&title=%20%20%200%2f61"/>

<details markdown="1"><summary markdown="1">Click to expand file tree...</summary>

- :black_large_square:  (0/31, 0%)
- :black_large_square: A_Drive_Frame_Lower_x1
- :black_large_square: A_Drive_Frame_Upper_x1
- :black_large_square: A_Idler_Lower_x1
- :black_large_square: A_Idler_Upper_x1
- :black_large_square: B_Drive_Frame_Lower_x1
- :black_large_square: B_Drive_Frame_Upper_x1
- :black_large_square: B_Idler_Lower_x1
- :black_large_square: B_Idler_Upper_x1
- :black_large_square: Front_Bed_Mount_x1
- :black_large_square: M2_Nut_Adapter_Rotated_x5
- :black_large_square: Power_Inlet_x1
- :black_large_square: Raspberry_Pi_3b_Mount_x1
- :black_large_square: Rear_Bed_Mount_Left_x1
- :black_large_square: Rear_Bed_Mount_Right_x1
- :black_large_square: Skr_E3_Mounting_Bracket_x1
- :black_large_square: XY_Joint_Left_Lower_x1
- :black_large_square: XY_Joint_Left_Upper_x1
- :black_large_square: XY_Joint_Right_Lower_x1
- :black_large_square: XY_Joint_Right_Upper_x1
- :black_large_square: [a]_9mm_Spacer_x6
- :black_large_square: [a]_A_Drive_Tensioner_x1
- :black_large_square: [a]_B_Drive_Tensione_x1
- :black_large_square: [a]_Foot_Front_x2
- :black_large_square: [a]_Foot_Rear_Left_x1
- :black_large_square: [a]_Foot_Rear_Right_x1
- :black_large_square: [a]_Railstops_x6
- :black_large_square: [a]_Tensioner_Knob_x2
- :black_large_square: [a]_Thumb_Nut_x3
- :black_large_square: [a]_X_Endstop_Bumper_x1
- :black_large_square: [a]_Z_Endstop_Mount_x1
- :black_large_square: [a]_Z_Motor_Mount_x1
- :black_large_square: Panel_Mounting (0/20, 0%)
  - :black_large_square: For_2.5mm_Panels (0/5, 0%)
    - :black_large_square: 2point5mm_Bottom_Corner_Rear_mirror_x1
    - :black_large_square: 2point5mm_Bottom_Corner_Side_mirror_x1
    - :black_large_square: 2point5mm_Top_Corner_Rear_mirror_x1
    - :black_large_square: 2point5mm_Top_Corner_Rear_x1
    - :black_large_square: 2point5mm_Top_Corner_Side_mirror_x1
  - :black_large_square: For_3mm_Panels (0/15, 0%)
    - :black_large_square: 3mm_Bottom_Corner_Front_x1
    - :black_large_square: 3mm_Bottom_Corner_Rear_mirror_x1
    - :black_large_square: 3mm_Bottom_Corner_Rear_x1
    - :black_large_square: 3mm_Bottom_Corner_Side_mirror_x1
    - :black_large_square: 3mm_Bottom_Corner_Side_x2
    - :black_large_square: 3mm_Hinge_Bottom_A_x1
    - :black_large_square: 3mm_Hinge_Bottom_B_x1
    - :black_large_square: 3mm_Hinge_Top_A_x1
    - :black_large_square: 3mm_Hinge_Top_B_x1
    - :black_large_square: 3mm_Middle_Clip_x9
    - :black_large_square: 3mm_Top_Corner_Front_x1
    - :black_large_square: 3mm_Top_Corner_Rear_mirror_x1
    - :black_large_square: 3mm_Top_Corner_Rear_x1
    - :black_large_square: 3mm_Top_Corner_Side_mirror_x1
    - :black_large_square: 3mm_Top_Corner_Side_x2
- :black_large_square: Toolheads (0/8, 0%)
  - :black_large_square: Mini_Afterburner (0/8, 0%)
    - :black_large_square: Guidler_DD_x1
    - :black_large_square: Latch_DD_x1
    - :black_large_square: Latch_Shuttle_DD_x1
    - :black_large_square: Motor_Frame_x1
    - :black_large_square: Dragon_Toolhead_DD (0/2, 0%)
      - :black_large_square: [a]_Cowling_dragon_x1
      - :black_large_square: [a]_Mid_Body_Dragon_x1
    - :black_large_square: Dragonfly_BMO_Toolhead_DD (0/1, 0%)
      - :black_large_square: [a]_Mid_Body_BMO_x1
    - :black_large_square: Mosquito_Toolhead_DD (0/1, 0%)
      - :black_large_square: [a]_Mid_Body_Mosquito_x1
- :black_large_square: Tools (0/1, 0%)
  - :black_large_square: AB_pulley_jig_x1
- :black_large_square: Tophat (0/1, 0%)
  - :black_large_square: Lower_Corner_1_and_3_Clip_x2
</details>

<!-- END_STATS -->

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
