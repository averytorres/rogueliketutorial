import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity
from item_choice_definition.weapon_choices_values.knive_choices import get_knife_choices
from item_choice_definition.weapon_choices_values.sword_choices import get_sword_choices
from item_choice_definition.weapon_choices_values.greatsword_choices import get_greatsword_choices
from item_choice_definition.weapon_choices_values.backsword_choices import get_backsword_choices
from item_choice_definition.weapon_choices_values.axe_choices import get_axe_choices
from item_choice_definition.weapon_choices_values.club_choices import get_club_choices
from item_choice_definition.weapon_choices_values.polearm_choices import get_polearm_choices
from item_choice_definition.weapon_choices_values.bow_choices import get_bow_choices
from item_choice_definition.weapon_choices_values.throwing_choices import get_throwing_choices
from item_choice_definition.weapon_choices_values.arrow_choices import get_arrow_choices


def get_foot_armor_choice(item_choice, x, y):
    suffix = '-foot_armor'
    display_icon = 'b'
    display_color = libtcod.darker_amber
    equipment_slot = EquipmentSlots.FEET

    disp_name = item_choice.replace(suffix,"")
    item = None

    if item_choice == 'Black Boots' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=3)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Elven Boots' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Dwarvish Iron Shoes' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Boots of Jumping' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Boots of Levitation' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Speed Boots' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Silk Shoes' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Low Boots' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)

    return item
