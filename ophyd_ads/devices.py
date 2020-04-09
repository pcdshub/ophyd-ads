from ophyd import Component as Cpt
from ophyd import Device

from .signal import AdsSignal


class NcAxis(Device):
    act_acc = Cpt(AdsSignal, 'ActAcc')
    act_pos = Cpt(AdsSignal, 'ActPos')
    act_pos_modulo = Cpt(AdsSignal, 'ActPosModulo')
    act_torque = Cpt(AdsSignal, 'ActTorque')
    act_velo = Cpt(AdsSignal, 'ActVelo')
    axis_state = Cpt(AdsSignal, 'AxisState')
    cmd_no = Cpt(AdsSignal, 'CmdNo')
    control_d_word = Cpt(AdsSignal, 'ControlDWord')
    couple_state = Cpt(AdsSignal, 'CoupleState')
    ctrl_output = Cpt(AdsSignal, 'CtrlOutput')
    drive_output = Cpt(AdsSignal, 'DriveOutput')
    err_state = Cpt(AdsSignal, 'ErrState')
    # from_plc = Cpt(AdsSignal, 'FromPlc')
    homing_state = Cpt(AdsSignal, 'HomingState')
    override_v = Cpt(AdsSignal, 'OverrideV')
    pos_diff = Cpt(AdsSignal, 'PosDiff')
    pos_diff_couple = Cpt(AdsSignal, 'PosDiffCouple')
    set_acc = Cpt(AdsSignal, 'SetAcc')
    set_pos = Cpt(AdsSignal, 'SetPos')
    set_pos_modulo = Cpt(AdsSignal, 'SetPosModulo')
    set_torque = Cpt(AdsSignal, 'SetTorque')
    set_velo = Cpt(AdsSignal, 'SetVelo')
    state_d_word = Cpt(AdsSignal, 'StateDWord')
    # to_plc = Cpt(AdsSignal, 'ToPlc')
