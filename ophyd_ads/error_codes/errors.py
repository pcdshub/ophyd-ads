errors = {
    19200: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Axis was stopped" The axis was stopped during travel to the target position. The axis may have been stopped with a PLC command via ADS, a call via AXFNC, or by the System Manager.',
    },
    19201: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Axis cannot be started" The axis cannot be started because: \n\n▪\nthe axis is in error status,\n\n\n▪\nthe axis is executing another command,\n\n\n▪\nthe axis is in protected mode,\n\n\n▪\nthe axis is not ready for operation.',
    },
    19202: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Control mode not permitted" No target position control, and no position range control.',
    },
    19203: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Axis is not moving" The position and velocity can only be restarted while the axis is physically in motion.',
    },
    19204: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Wrong mode for RestartPosAndVelo" Wrong mode.',
    },
    19205: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Command not permitted"\n\n\n▪\nContinuous motion in an unspecified direction\n\n\n▪\nRead/Write parameters: type mismatch',
    },
    19206: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Parameter incorrect"\n\n\n▪\nIncorrect override: > 100% or < 0%\n\n\n▪\nIncorrect gear ratio: RatioDenominator = 0',
    },
    19207: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Timeout axis function block"\n\nAfter positioning, all "MC_Move..." blocks check whether positioning was completed successfully. In the simplest case, the "AxisHasJob" flag of the NC axis is checked, which initially signifies that positioning was logically completed. Depending on the parameterization of the NC axis, further checks (quality criteria) are used:\n\n▪\n"Position range monitoring"If position range monitoring is active, the system waits for feedback from the NC. After positioning, the axis must be within the specified positioning range window. If necessary, the position controller ensures that the axis is moved to the target position. If the position controller is switched off (Kv=0) or weak, the target may not be reached.\n\n\n▪\n"Target position monitoring"If target position monitoring is active, the system waits for feedback from the NC. After positioning, the axis must be within the specified target position window for at least the specified time. If necessary, the position controller ensures that the axis is moved to the target position. If the position controller is switched off (Kv=0) or weak, the target may not be reached. Floating position control may lead to the axis oscillating around the window but not remaining inside the window.\n\nIf the axis is logically at the target position (logical standstill) but the parameterized position window has not been reached, monitoring of the above-mentioned NC feedback is aborted with error 19207 (0x4B07) after a constant timeout of 6 seconds.',
    },
    19208: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Axis is in protected mode" The axis is in protected mode ( e.g. coupled) and cannot be moved.',
    },
    19209: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Axis is not ready" The axis is not ready and cannot be moved.',
    },
    19210: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Error during referencing" Referencing (homing) of the axis could not be started or was not successful.',
    },
    19211: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Incorrect definition of the trigger input" The definition of the trigger signal for block MC_TouchProbe is incorrect. The defined encoder-ID, the trigger signal or the trigger edge are invalid.',
    },
    19212: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"Position latch was disabled" The function block MC_TouchProbe has detected that a measuring probe cycle it had started was disabled. The reason may be an axis reset, for example.',
    },
    19213: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "‘NC status feedback timeout’  A function was successfully sent from the PLC to the NC. An expected feedback in the axis status word has not arrived.",
    },
    19214: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"Additional product not installed" The function is available as an additional product but is not installed on the system.',
    },
    19215: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"No NC Cycle Counter Update" – The NcToPlc Interface or the NC Cycle Counter in the NcToPlc Interface was not updated.',
    },
    19216: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"M-function query missing" This error occurs if the M-function was confirmed, but the request bit was not set.',
    },
    19217: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Zero offset index is outside the range" The index of the zero offset is invalid.',
    },
    19218: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"R-parameter index or size is invalid" This error occurs if the R-parameters are written or read but the index or size are outside the range.',
    },
    19219: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Index for tool description is invalid"',
    },
    19220: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"Version of the cyclic channel interface does not match the requested function or the function block" This error occurs if an older TwinCAT version is used to call new functions of a later TcNci.lib version.',
    },
    19221: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"Channel is not ready for the requested function" The requested function cannot be executed, because the channel is in the wrong state. This error occurs during reverse travel, for example, if the axis was not stopped with ItpEStop first.',
    },
    19222: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"Requested function is not activated" The requested function requires explicit activation.',
    },
    19223: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"Axis is already in another group" The axis has already been added to another group.',
    },
    19224: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"Block search could not be executed successfully" The block search has failed. \nPossible causes:\n\n▪\nInvalid block number',
    },
    19225: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Invalid block search parameter" This error occurs if the FB ItpBlocksearch is called with invalid parameters (e.g. E_ItpDryRunMode, E_ItpBlockSearchMode)',
    },
    19232: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"Cannot add all axes" This error occurs if an auxiliary axis is to be added to an interpolation group, but the function fails. It is likely that a preceding instruction of an auxiliary axis was skipped.',
    },
    19248: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Pointer is invalid" A pointer to a data structure is invalid, e.g. Null \n\n▪\nData structure MC_CAM_REF was not initialized',
    },
    19249: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Memory size invalid" The specification of the memory size (SIZE) for a data structure is invalid. \n\n▪\nThe value of the size parameter is 0 or less than the size of one element of the addressed data structure.\n\n\n▪\nThe value of the size parameter is less than the requested amount of data.\n\n\n▪\nThe value of the size parameter does not match other parameters as number of points, number of rows or number of columns.',
    },
    19250: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Cam table ID is invalid" The ID of a cam table is not between 1 and 255.',
    },
    19251: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Point ID is invalid" The ID of a point (sampling point) of a motion function is less than 1.',
    },
    19252: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Number of points is invalid" The number of points (sampling points) of a cam plate to be read or written is less than 1.',
    },
    19253: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"MC table type is invalid" The type of a cam plate does not match the definition MC_TableType.',
    },
    19254: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Number of rows invalid" The number of rows (sampling points) of a cam table is less than 1.',
    },
    19255: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Number of columns invalid" The number of columns of a cam table is invalid. \n\n▪\nThe number of columns of a motion function is not equal 1\n\n\n▪\nThe number of columns of a standard cam table is not equal 2\n\n\n▪\nThe number of columns does not match another parameter (ValueSelectMask)',
    },
    19256: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Step size invalid". The increment for the interpolation is invalid, e.g. less than or equal to zero.',
    },
    19264: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": '"Terminal type not supported" The terminal used is not supported by this function block.',
    },
    19265: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": '"Register read/write error" This error implies a validity error.',
    },
    19266: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": '"Axis is enabled" The axis is enabled but should not be enabled for this process.',
    },
    19267: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Incorrect size of the compensation table" The specified table size (in bytes) does not match the actual size',
    },
    19268: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "The minimum/maximum position in the compensation table does not match the position in the table description (ST_CompensationDesc)",
    },
    19269: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Not implemented" The requested function is not implemented in this combination',
    },
    19296: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": '"Motion command did not become active" A motion command has been started and has been buffered and confirmed by the NC. Nevertheless, the motion command did not become active (possibly due to a terminating condition or an internal NC error).',
    },
    19297: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": '"Motion command could not be monitored by the PLC" A motion command has been started and has been buffered and confirmed by the NC. The PLC has not been able to monitor the execution of this command and the execution status is unclear since the NC is already executing a more recent command. The execution state is unclear. This error may come up with very short buffered motion commands which are executed during one PLC cycle.',
    },
    19298: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": '"Buffered command was terminated with an error" A buffered command was terminated with an error. The error number is not available, because a new command is already being executed.',
    },
    19299: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": '"Buffered command was completed without feedback" A buffered command was completed but there was no feedback to indicate success or failure.',
    },
    19300: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": "\" 'BufferMode' is not supported by the command\" The 'BufferMode' is not supported by this command.",
    },
    19301: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": '"Command number is zero" The command number for queued commands managed by the system unexpectedly has the value 0.',
    },
    19302: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": '"Function block was not called cyclically" The function block was not called cyclically. The command execution could not be monitored by the PLC, because the NC was already executing a subsequent command. The execution state is unclear.',
    },
    19313: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"Invalid NCI entry type". The FB FB_NciFeedTablePreparation was called with an unknown nEntryType.',
    },
    19314: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": '"NCI feed table full" The table is full, and the entry is therefore not accepted.Remedy:Transfer the context of the table with FB_NciFeedTable to the NC-Kernel. If bFeedingDone = TRUE, the table can be reset in FB_NciFeedTablePreparation with bResetTable and then filled with new entries.',
    },
    19315: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "internal error",
    },
    19316: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": '"ST_NciTangentialFollowingDesc: tangential axis is not an auxiliary axis" The entry for tangential following contains a tangential axis that is not an auxiliary axis.',
    },
    19317: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "ST_NciTangentialFollowingDesc: nPathAxis1 or nPathAxis2 is not a path axis. It is therefore not possible to determine the plane.",
    },
    19318: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "ST_NciTangentialFollwoingDesc: nPathAxis1 and nPathAxis2 are the same. It is therefore not possible to determine the plane.",
    },
    19319: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "ST_NciGeoCirclePlane: Circle incorrectly parameterized",
    },
    19320: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "Internal error during calculation of tangential following",
    },
    19321: {
        "Category": "NC-PLC Errors",
        "Error type": "Monitoring",
        "Description": "Tangential following: Monitoring of the deviation angle was activated during activation of tangential following (E_TfErrorOnCritical1), and an excessively large deviation angle was detected in the current segment.",
    },
    19322: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "not implemented",
    },
    19323: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "Tangential following: the radius of the current arc is too small",
    },
    19324: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "FB_NciFeedTablePreparation: pEntry is NULL",
    },
    19325: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "FB_NciFeedTablePreparation: the specified nEntryType does not match the structure type",
    },
    19326: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "ST_NciMFuncFast and ST_NciMFuncHsk: the requested M-function is not between 0 and 159",
    },
    19327: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "ST_NciDynOvr: the requested value for the dynamic override is not between 0.01 and 1",
    },
    19328: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "ST_NciVertexSmoothing: invalid parameter. This error is generated if a negative smoothing radius or an unknown smoothing type is encountered.",
    },
    19329: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "FB_NciFeedTablePrepartion: The requested velocity is not in the valid range",
    },
    19330: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "ST_Nci*: invalid parameter",
    },
    19360: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "KinGroup error: the kinematic group is in an error state.\nThis error may occur if the kinematic group is in an error state or an unexpected state when it is called (e.g. simultaneous call via several FB instances).",
    },
    19361: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "KinGroup timeout: timeout during call of a kinematic block",
    },
    19344: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "Determined drive type is not supported",
    },
    19345: {
        "Category": "NC-PLC Errors",
        "Error type": "Parameter",
        "Description": "Direction is impermissible",
    },
    19346: {
        "Category": "NC-PLC Errors",
        "Error type": "",
        "Description": "SwitchMode is impermissible",
    },
    19347: {
        "Category": "NC-PLC Errors",
        "Error type": "",
        "Description": "Mode for the parameter handling is impermissible",
    },
    19348: {
        "Category": "NC-PLC Errors",
        "Error type": "",
        "Description": "Parameterization of the torque limits is inconsistent",
    },
    19349: {
        "Category": "NC-PLC Errors",
        "Error type": "",
        "Description": "Parameterization of the position lag limit is impermissible (<=0).",
    },
    19350: {
        "Category": "NC-PLC Errors",
        "Error type": "",
        "Description": "Parameterization of the distance limit is impermissible (<0)",
    },
    19351: {
        "Category": "NC-PLC Errors",
        "Error type": "",
        "Description": "An attempt was made to back up parameters again, although they have already been backed up.",
    },
    19352: {
        "Category": "NC-PLC Errors",
        "Error type": "",
        "Description": "An attempt was made to restore parameters, although none have been backed up.",
    },
    19376: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "The current axis position or the axis position resulting from the new position offset exceeds the valid range of values.",
    },
    19377: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "The new position offset exceeds the valid range of values [AX5000: 2^31]",
    },
    19378: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "The current axis position or the axis position resulting from the new position offset falls below the valid range of values.",
    },
    19379: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "The new position offset falls below the valid range of values [AX5000: -2^31]",
    },
    19380: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "The activated feedback and/or storage location (AX5000: P-0-0275) differ from the parameterization on the function block.",
    },
    19381: {
        "Category": "NC-PLC Errors",
        "Error type": "Function",
        "Description": "Reinitialisation of the Nc actual position has failed.\ne.g. reference system = “ABSOLUTE (with single overflow)” & software end position monitoring is disabled.",
    },
    33056: {
        "Category": "Further Error Codes",
        "Error type": "Environment",
        "Description": "Invalid configuration for Object (e.g. in System Manager)",
    },
    33057: {
        "Category": "Further Error Codes",
        "Error type": "Environment",
        "Description": "Invalid environment for Object (e.g. TcCom-Object's Hierarchy or missing/faulty Objects)",
    },
    33058: {
        "Category": "Further Error Codes",
        "Error type": "Environment",
        "Description": "Incompatible Driver or Object",
    },
    33077: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Function Block Inputs are inconsitent.Some Inputs of the Function Block are inconsistent during. Probably Communicator and its IID, which both have to be set or unset.",
    },
    33083: {
        "Category": "Further Error Codes",
        "Error type": "Parameter",
        "Description": "Transition Mode is invalid",
    },
    33084: {
        "Category": "Further Error Codes",
        "Error type": "Parameter",
        "Description": "BufferMode is invalid",
    },
    33085: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Only one active Instance of Function Block per Group is allowed.",
    },
    33086: {
        "Category": "Further Error Codes",
        "Error type": "State",
        "Description": "Command is not allowed in current group state.",
    },
    33087: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Slave cannot synchronize.The slave cannot reach the SlaveSyncPosition by the time the master has reached the MasterSyncPos.",
    },
    33088: {
        "Category": "Further Error Codes",
        "Error type": "Parameter",
        "Description": "Invalid value for one or more of the dynamic parameters (A, D, J).",
    },
    33089: {
        "Category": "Further Error Codes",
        "Error type": "Parameter",
        "Description": "IdentInGroup is invalid.",
    },
    33090: {
        "Category": "Further Error Codes",
        "Error type": "Parameter",
        "Description": "The number of axes in the group is incompatible with the axes convention.",
    },
    33091: {
        "Category": "Further Error Codes",
        "Error type": "Communication",
        "Description": "Function Block or respective Command is not supported by Target.",
    },
    33093: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Mapping of Cyclic Interface between Nc and Plc missing (e.g. AXIS_REF, AXES_GROUP_REF, ...).",
    },
    33094: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Invalid Velocity ValueThe velocity was not set or the entered value is invalid",
    },
    33096: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Invalid Input Value",
    },
    33097: {
        "Category": "Further Error Codes",
        "Error type": "Parameter",
        "Description": "Unsupported Dynamics for selected Group Kernel",
    },
    33098: {
        "Category": "Further Error Codes",
        "Error type": "Parameter",
        "Description": "The programmed position dimension incompatible with the axes convention.",
    },
    33099: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Path buffer is invalid. E.g. because provided buffer has invalid address or is not big enough",
    },
    33100: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Path does not contain any element",
    },
    33101: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Provided Path buffer is too small to store more Path Elements",
    },
    33102: {
        "Category": "Further Error Codes",
        "Error type": "Parameter",
        "Description": "Dimension or at least one Value of Transition Parameters is invalid",
    },
    33103: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Invalid or Incomplete Input Array",
    },
    33104: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Path length is zero",
    },
    33105: {
        "Category": "Further Error Codes",
        "Error type": "State",
        "Description": "Command is not allowed in current axis state.",
    },
    33106: {
        "Category": "Further Error Codes",
        "Error type": "State",
        "Description": "TwinCAT System is shutting down and cannot complete request.",
    },
    33120: {
        "Category": "Further Error Codes",
        "Error type": "NC Programming",
        "Description": "Circle Specification in Path is invalid.The specification of a circle segment in the programmed interpolated path (e.g. via MC_MovePath) has an invalid or ambiguous descripition. Probably its center cannot be determined reliably.",
    },
    33121: {
        "Category": "Further Error Codes",
        "Error type": "NC Programming",
        "Description": "Maximum stream lines reached.The maximum number of stream lines is limited. Please refer to function block documentation for details.",
    },
    33123: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Invalid First Segment.The corresponding element can only be analyzed with a well-defined start point.",
    },
    33124: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Invalid auxiliary point.The auxiliary point is not well-defined.",
    },
    33126: {
        "Category": "Further Error Codes",
        "Error type": "FunctionBlock",
        "Description": "Invalid parameter for GapControlModeInvalid parameter for GapControlMode, most likely in combination with the group parameter GapControlDirection",
    },
    33127: {
        "Category": "Further Error Codes",
        "Error type": "External",
        "Description": "Group got unsupported Axis Event (e.g. State Change)Group got unsupported Axis Event (e.g. State Change e.g. triggered by a Single Axis Reset)",
    },
    36726: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36727: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36728: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36729: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36730: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36731: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36732: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36733: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36734: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36735: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36736: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36737: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36738: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36739: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36740: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36741: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36742: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36743: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36744: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36745: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36746: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36747: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36748: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36749: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36750: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36751: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36752: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36753: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36754: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36755: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36756: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36757: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36758: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36759: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36760: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36761: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36762: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36763: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36764: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36765: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36766: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36767: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36768: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36769: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36770: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36771: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36772: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36773: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36774: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36775: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36776: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36777: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36778: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36779: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36780: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36781: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36782: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36783: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36784: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36785: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36786: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36787: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36788: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36789: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36790: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36791: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36792: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36793: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36794: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36795: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36796: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36797: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36798: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36799: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36800: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36801: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36802: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36803: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36804: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36805: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36806: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36807: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36808: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36809: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36810: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36811: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36812: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36813: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36814: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36815: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36816: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36817: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36818: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36819: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36820: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36821: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36822: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36823: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36824: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36825: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36826: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36827: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36828: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36829: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36830: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36831: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36832: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36833: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36834: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36835: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36836: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36837: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36838: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36839: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36840: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36841: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36842: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36843: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36844: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36845: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36846: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36847: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36848: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36849: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36850: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36851: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36852: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36853: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36854: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36855: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36856: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36857: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36859: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36860: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36861: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    36862: {
        "Category": "Further Error Codes",
        "Error type": "Internal",
        "Description": "Unexpected Internal Error",
    },
    16896: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Group ID not allowed" The value for the group ID is not allowed, e.g. because it has already been assigned, is less than or equal to zero, or is greater than 255.',
    },
    16897: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Group type not allowed" The value for the group type is unacceptable because it is not defined. Type 1: PTP group with slaves (servo) Type 4: DXD group with slaves (3D group) Type 5: High/low speed group Type 6: Stepper motor group Type 9: Encoder group with slaves (servo)…',
    },
    16898: {
        "Category": "Group Errors",
        "Error type": "Initialization",
        "Description": '"Master axis index not allowed" The value for the master axis index in an interpolating 3D group is not allowed, because, for instance, it has gone outside the value range. Index 0: X axis (first master axis) Index 1: Y axis (second master axis) Index 2\xa0: Z axis (third master axis)',
    },
    16899: {
        "Category": "Group Errors",
        "Error type": "Initialization",
        "Description": '"Slave axis index not allowed" (INTERNAL ERROR) The value for the slave axis index in a group is not allowed, because, for instance, it has passed outside the value range, the slave location to be used when inserting a new slave connection is already occupied, or because no slave is present when such a connection is being removed. Index 0: First slave axis Index 1: Second slave axis Index 2: etc.',
    },
    16900: {
        "Category": "Group Errors",
        "Error type": "Initialization",
        "Description": '"INTERNAL ERROR" (GROUPERR_INTERNAL)',
    },
    16901: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid cycle time for statement execution task (SAF)" The value of the cycle time for the NC block execution task (SAF 1/2) is not allowed, because it has passed outside the value range.',
    },
    16902: {
        "Category": "Group Errors",
        "Error type": "Initialization",
        "Description": '"GROUPERR_RANGE_MAXELEMENTSINAXIS "',
    },
    16903: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid cycle time for the statement preparation task (SVB)" The value of the cycle time for the NC statement preparation task (SVB 1/2) is not allowed, because it has passed outside the value range.',
    },
    16904: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Single step mode not allowed" The flag for the activation or deactivation of single step mode is not allowed. Value 0: Passive (buffered operation) Value 1: Active (single-block operation)',
    },
    16905: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Group deactivation not allowed" (INTERNAL ERROR) The flag for the deactivation or activation of the complete group is not allowed. Value 0: Group active Value 1: Group passive',
    },
    16906: {
        "Category": "Group Errors",
        "Error type": "Initialization",
        "Description": '"Statement execution state (SAF state) not allowed" (INTERNAL ERROR) The value for the state of the block execution state machine (SAF state) is not allowed. This error occurs on passing outside the range of values, or if the state machine enters an error state.',
    },
    16907: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Channel address" The group does not have a channel, or the channel address has not been initialized.',
    },
    16908: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Axis address (master axis)" The group does not have a master axis (or axes) or the axis address(es) has (have) not been initialized.',
    },
    16909: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Master axis address" A new master/slave coupling is to be inserted into the group, but there is no valid address for the leading master axis.',
    },
    16910: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Slave axis address" A master/slave coupling is to be inserted into the group, but there is no valid address for the slave axis.',
    },
    16911: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Slave set value generator address" A master/slave coupling is to be inserted into the group, but there is no valid address for the slave set value generator.',
    },
    16912: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Encoder address" An axis in the group does not have an encoder, or the encoder address has not been initialized.',
    },
    16913: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Controller address" An axis in the group does not have a controller, or the controller address has not been initialized.',
    },
    16914: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Drive address" An axis in the group does not have a drive, or the drive address has not been initialized.',
    },
    16915: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"GROUPERR_ADDR_MASTERGENERATOR"',
    },
    16916: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Axis interface NC to PLC address" Group/axis does not have an axis interface from the NC to the PLC, or the axis interface address has not been initialized.',
    },
    16917: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Slave axis address" An existing master/slave coupling is to be removed from the group, but there is no valid address for the slave axis.',
    },
    16918: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Table address unknown" The table, respectively the table ID, is unknown. This table is used for the master/slave coupling or for the characteristic curve.',
    },
    16919: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"NcControl address" The NcControl address has not been initialized.',
    },
    16920: {
        "Category": "Group Errors",
        "Error type": "Initialization",
        "Description": '"Axis is blocked for commands while persistent NC data are queued" Axis is blocked for commands while waiting for valid IO data to accept the queued persistent NC data.',
    },
    16921: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"The scaling mode MASTER-AUTOOFFSET is invalid because no reference table was found". The used scaling mode MASTER-AUTOOFFSET is invalid in this context because an existing reference table is missing. This error can occur for example when adding cam tables without a unique reference to an existing cam table.',
    },
    16922: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"The master axis start position does not permit synchronization" When a slave axis is being coupled on, the position of the master axis does not permit synchronization at the given synchronization positions.',
    },
    16923: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Slave coupling factor (gearing factor) of 0.0 is not allowed" A master/slave coupling with a gearing factor of 0.0 is being created. This value is not allowed, since it does not correspond to any possible coupling, and division will generate an FPU exception.',
    },
    16924: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Insertion of master axis into group not allowed" A master axis is to be inserted into a group at a location that is already occupied by another master axis. Maybe the reconfiguration cannot be done, because this axis has got an existing slave coupling. This master/slave coupling must be revoked before.',
    },
    16925: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Deletion of master axis from group not allowed" (INTERNAL ERROR) A master axis is to be removed from a location in a group that is not in fact occupied by master axis.',
    },
    16926: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Function/feature is not supported from the setpoint generator A function or feature is not supported from the setpoint generator (e.g. PTP master setpoint generator). This can be in general or only in a special situation.',
    },
    16927: {
        "Category": "Group Errors",
        "Error type": "Initialization",
        "Description": '"Group initialization" Group has not been initialized. Although the group has been created, the rest of the initialization has not been performed (1. Initialization of group I/O, 2. Initialization of group, 3. Reset group).',
    },
    16928: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Group not ready / group not ready for new task" The group is being given a new task while it is still in the process of executing an existing task. This request is not allowed because it would interrupt the execution of the previous task. The new task could, for instance, be a positioning command, or the "set actual position" function. Precisely the converse relationships apply for the "set new end position" function. In that case, the group/axis must still be actively moving in order to be able to cause a change in the end position.',
    },
    16929: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Requested set velocity is not allowed" The value requested for the set velocity of a positioning task is less than or equal to zero, larger than the "maximum velocity" (see axis parameters), or, in the case of servo-drives, is larger than the "reference velocity" of the axis (see drive parameters).',
    },
    16930: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Requested target position is not allowed (master axis)" The requested value for the target position of a positioning task is not within the software end locations. In other words, it is either less than the minimum software end location or larger than the maximum software end location. This check is only carried out if the relevant end position monitoring is active.',
    },
    16931: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"No enable for controller and/or feed (Master axis)" The axis enables for the master axis needed for positioning are not present. This can involve the controller enable and/or the relevant, direction-dependent feed enable (see axis interface PlcToNc).',
    },
    16932: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Movement smaller than one encoder increment" (INTERNAL ERROR) The distance that a group/axis is supposed to move is smaller than the physical significance of one encoder increment. In other words the movement is smaller than the scaling factor of the axis. The reaction to this is that the axis is reported as having logically finished without having actively moved. This means that an external error is not generated for the user. This error is also issued for high/low speed axes if a loop movement with nonzero parameters is smaller than the sum of the creeping and braking distances. In such a case it is not meaningful to either exceed or to fail to reach the target position.',
    },
    16933: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Drive not ready during axis start" During an axis start it is ascertained that the drive is not ready. The following are possible causes: - the drive is in the error state (hardware error) - the drive is in the start-up phase (e.g. after an axis reset that was preceded by a hardware error) - the drive is missing the controller enable (ENABLE) Note: The time required for "booting" a drive after a hardware fault can amount to several seconds.',
    },
    16934: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Invalid parameters of the emergency stop." Either, both, the deceleration and the jerk are less than zero or one of the parameters is weaker than the corresponding parameter of the start data.',
    },
    16935: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"The setpoint generator is inactive such that no instructions are accepted."',
    },
    16936: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Requested traverse distance is not allowed" The requested traverse distance or looping distance is smaller than the braking distance of the two/speed axis.',
    },
    16937: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Requested target position is not allowed (slave axis)" The value for the target position of a positioning task when calculated for the slave axis is not within the software end locations. In other words, it is either less than the minimum software end location or larger than the maximum software end location. This check is only carried out if the relevant end position monitoring is active.',
    },
    16938: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"No enable for controller and/or feed (slave axis)" The axis enables for one or more coupled slave axes needed for positioning are not present. This can involve the controller enable and/or the relevant, direction-dependent feed enable (see axis interface PlcToNc).',
    },
    16939: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"The activation position (position threshold) is out of range of the actual positioning" The activation position (position threshold) of a new axis command (e.g. "new velocity activated at a position") is out of range. E.g. the activation position is before the actual position or behind the target position.',
    },
    16940: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"The start or activation data of the external setpoint generation are not valid" This may be caused through: 1. The external setpoint generation is active and a new activation with a start type (1: absolute, 2: relative) unequal to the current one is send. 2. The internal setpoint generation is active (e.g. PTP) and the external one is activated with the type absolute (two setpoint generators of the type absolute are not possible).',
    },
    16941: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": "\"Velocity is not constant\" For changing the dynamic parameter 'acceleration' und 'deceleration' the axis has to be in dynamic state without acceleration and deceleration (that means constant velocity).",
    },
    16942: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Jerk less than or equal to 0.0 is not allowed" A value less than or equal to 0.0 for the jerk (PTP and CNC) is not allowed, since the jerk is by definition positive, and with a jerk of 0.0, division will generate an FPU exception.',
    },
    16943: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Acceleration less than or equal to 0.0 is not allowed" A value less than or equal to 0.0 for the acceleration (PTP and CNC) is not allowed, since the acceleration is positive by definition, and an acceleration of 0.0 will not allow a motion to be generated.',
    },
    16944: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Absolute deceleration value less than or equal to 0.0 is not allowed" A value less than or equal to 0.0 for the absolute value of the deceleration (PTP and CNC) is not allowed, since the absolute value of the deceleration is positive by definition, and an absolute value of the deceleration of 0.0 will not allow a motion to be generated.',
    },
    16945: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Set velocity less than or equal to 0.0 is not allowed" A value less than or equal to 0.0 or outside the range from 10-3 up to 10+10 for the set velocity (PTP and CNC) is not allowed, since the set velocity is by definition strictly positive, and with a set velocity of 0.0, division will generate an FPU exception.',
    },
    16946: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Loss of precision when trying a positioning" The positioning is so long in space or time that decimal parts loose there relevance LOSS_OF_PRECISION).',
    },
    16947: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Cycle time less than or equal to 0.0 is not allowed" A value less than or equal to 0.0 for the cycle time (PTP and CNC) is not allowed, since the cycle time is by definition strictly positive, and with a cycle time of 0.0, division will generate an FPU exception.',
    },
    16948: {
        "Category": "Group Errors",
        "Error type": "Internal",
        "Description": '"PTP data type <intasdouble> range exceeded" Such extreme parameters have been supplied for the start task, the override or the new target position that the internal data type loses its precision.',
    },
    16949: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"PTP LHL velocity profile cannot be generated" (INTERNAL ERROR) Such extreme parameters have been supplied for the start task, the override or the new target position that it is not possible to generate a velocity profile of the type LHL (Low-High-Low).',
    },
    16950: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"PTP HML velocity profile cannot be generated" (INTERNAL ERROR) Such extreme parameters have been supplied for the override or the new target position that it is not possible to generate a velocity profile of the type HML (High-Middle-Low).',
    },
    16951: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Start data address is invalid" The address of the start data is invalid.',
    },
    16952: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Velocity override (start override) is not allowed" The value for the velocity override is not allowed, because it is less than 0.0% or more than 100.0% (see axis interface PlcToNc). Here, 100.0 % corresponds to the integral value 1000000 in the axis interface. Value range: [0 ... 1000000]',
    },
    16953: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Start type not allowed" The start type supplied does not exist.',
    },
    16954: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Velocity overflow (overshoot in the velocity)" The new dynamic with the parameterized jerk is so weak that a velocity overflow will occur (overshoot in the velocity). The command is therefore not supported.',
    },
    16955: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Start parameter for the axis structure is invalid" External or internal parameters for the start structure for a positioning task are invalid. Thus, for instance, the scaling factor, the SAF cycle time or the requested velocity may be less than or equal to zero, which is not allowed.',
    },
    16956: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Override generator initialization parameter invalid" One of the override generator (re)initialization parameters is invalid.',
    },
    16957: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Slave axis has not set value generator" (INTERNAL ERROR) It is found that a slave axis within a group does not have a valid slave generator (set value generator). A slave axis and a slave set value generator must always be present as a pair. This is an internal error.',
    },
    16958: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Table is empty" Either the SVB table or the SAF table does not contain any entries.',
    },
    16959: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Table is full" The SVB table or the SAF table has no more free lines.',
    },
    16960: {
        "Category": "Group Errors",
        "Error type": "Memory",
        "Description": '"No memory available" SVB memory allocation for dynamic entry in SAF table failed.',
    },
    16961: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Table already contains an entry" (INTERNAL ERROR) SAF table entry abandoned, because, incorrectly, an entry already exists.',
    },
    16962: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Stop is already active" The stop instruction is not forwarded, because it has already been activated.',
    },
    16963: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Compensation has not been carried out over the full compensation section" The compensations start parameters do not permit compensation over the full section to be compensated. For this reason the compensation will be carried out over a smaller section.',
    },
    16964: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Internal parameters for the compensation are invalid" (INTERNAL ERROR) Invalid internal parameters or start parameters of the lower-level generator.',
    },
    16965: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Compensation active" Start of compensation refused, because compensation is already active. It\'s also possible that the M/S axes are not active moved. Therefore an execution of the compensation is impossible.',
    },
    16966: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Compensation not active" Stop of compensation refused, because compensation is not active.',
    },
    16967: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Compensation type invalid" The type supplied for the section compensation is invalid. At the present time only compensation type 1 (trapezoidal velocity profile) is allowed.',
    },
    16968: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Axis address for compensation invalid" (INTERNAL ERROR) The address of the master of slave axis on which the section compensation is to act is invalid. This is an internal error.',
    },
    16969: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Invalid slave address" (INTERNAL ERROR) The slave address given for on-line coupling/decoupling is invalid.',
    },
    16970: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Coupling velocity invalid" The velocity of what is to become the master axis is 0, which means that on-line coupling is not possible.',
    },
    16971: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Coupling velocities not constant" The velocity of what is to become the master axis and the velocity of what is to become the slave axis are not constant, so that on-line coupling is not possible.',
    },
    16972: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Cycle time less than or equal to 0.0 is not allowed" A value less than or equal to 0.0 for the cycle time (Slave) is not allowed, since the cycle time is by definition strictly positive, and with a cycle time of 0.0, division will generate an FPU exception.',
    },
    16973: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Decoupling task not allowed" The slave axis is of such a type (e.g. a table slave) or is in such a state (master velocity 0) that on-line decoupling is not possible.',
    },
    16974: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Function not allowed" The function cannot logically be executed, e.g. some commands are not possible and not allowed for slave axes.',
    },
    16975: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"No valid table weighting has been set" The weighting factor of each table is 0, so that no table can be read.',
    },
    16976: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Axis type, actual position type or end position type is not allowed" The start type for a positioning task in invalid. Valid start types are ABSOLUTE (1), RELATIVE (2), CONTINUOUS POSITIVE (3), CONTINUOUS NEGATIVE (4), MODULO (5), etc. It is also possible that the types for setting a new actual position or for travel to a new end position are invalid.',
    },
    16977: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Function not presently supported" An NC function has been activated that is currently not released for use, or which is not even implemented. This can be a command which is not possible or not allowed for master axes.',
    },
    16978: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"State of state machine invalid" (INTERNAL ERROR) The state of an internal state machine is invalid. This is an internal error.',
    },
    16979: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Reference cam became free too soon" During the referencing process for an axis it is moved in the direction of the referencing cam, and is only stopped again when the cam signal is reached. After the axis has then also physically stopped, the referencing cam must remain occupied until the axis subsequently starts back down from the cam in the normal way.',
    },
    16980: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Clearance monitoring between activation of the hardware latch and appearance of the sync pulse" When the clearance monitoring is active, a check is kept on whether the number of increments between activation of the hardware latch and occurrence of the sync pulse (zero pulse) has become smaller than a pre-set value. This error is generated when that happens. (See parameters for the incremental encoder)',
    },
    16981: {
        "Category": "Group Errors",
        "Error type": "Memory",
        "Description": '"No memory available" The dynamic memory allocation for the set value generator, the SVB table or the SAF table has failed.',
    },
    16982: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"The table slave axis has no active table" Although the table slave axis has tables, none of the tables is designated as active. If this occurs during the run time the whole master/slave group is stopped by a run time error.',
    },
    16983: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Function not allowed" The requested function or the requested task is not logically allowed. An example for such an error message would be "set an actual position" for an absolute encoder (M3000, KL5001, etc.).',
    },
    16984: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Stopping compensation not allowed" It is not possible to stop the compensation, since compensation is already in the stopping phase.',
    },
    16985: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Slave table is being used" The slave table cannot be activated, because it is currently being used.',
    },
    16986: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Master or slave axis is processing a job (e.g. positioning command) while coupling is requested" A master/slave coupling of a certain slave type (e.g. linear coupling) cannot be executed. he master or intended slave axis is not in stand still state and is executing a job (e.g. positioning) at the same time as the coupling request received. For this couple type this is not allowed.',
    },
    16987: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Slave (start) parameter is incorrect" One of the slave start/coupling parameters is not allowed (Coupling factor is zero, the master position scaling of an cam is zero, etc.).',
    },
    16988: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Slave type is incorrect" The slave type does not match up to the (SVB) start type.',
    },
    16989: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Axis stop is already active" The axis stop/Estop is not initiated, because the stop/estop is already active.',
    },
    16990: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Maximum number of tables per slavegenerator reached" The maximum number of tables per slave generator is reached (e.g. "MC_MultiCamIn" is limited to 4 tables).',
    },
    16991: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"The scaling mode is invalid". The used scaling is invalid in this context. Either the mode is not defined or yet not implemented or however it cannot in this constellation be put into action. For example MASTER-AUTOOFFSET cannot be used when a cam table is coupled in relative mode because this is a contradiction. Further MASTER-AUTOOFFSET cannot be used when a cam table is coupled for the first time because a relationship to an existing reference table is missing.',
    },
    16992: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Controller enable" Controller enable for the axis or for a coupled slave axis is not present (see axis interface PlcToNc). This error occurs if the controller enable is withdrawn while an axis or a group of axes (also a master/slave group) is being actively positioned. The error also occurs if a PTP axis or a coupled slave axis is started without controller enable.',
    },
    16993: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Table not found" No table exists with the ID prescribed or the table ID is not unique.',
    },
    16994: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Incorrect table type" The table referred to in the function is of the incorrect type.',
    },
    16995: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Single step mode" This error occurs if single step mode is selected for a group or axis and a new task is requested while one of the individual tasks is still being processed.',
    },
    16996: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Group task unknown (asynchronous table entry)" The group has received a task whose type or sub-type is unknown. Valid tasks can be single or multi-dimensional positioning tasks (Geo 1D, Geo 3D), referencing tasks, etc.',
    },
    16997: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Group function unknown (synchronous function)" The group has received a function whose type is unknown. Valid functions are "Reset", "Stop", "New end position", "Start/stop section compensation", "Set actual position", "Set/reset referencing status" etc.',
    },
    16998: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Group task for slave not allowed" Group tasks are usually only possible for master axes, not for slave axes. A slave axis only moves as an indirect result of a positioning task given to its associated master axis. A slave can thus never directly be given a task. Exception: see axis parameter "Allow motion commands to slave axis".',
    },
    16999: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Group function for slave not allowed" Group functions are in principle only possible for master axes, not for slave axes. The only exception is represented by the "Start/stop section compensation" function, which is possible both for masters and for slaves. A slave cannot directly execute any other functions beyond this.',
    },
    17000: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"GROUPERR_GROUPFUNC_NOMOTION"',
    },
    17001: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Startposition=Setpoint Position" Invalid position parameters.',
    },
    17002: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Parameters of the delay-generator are invalid" Invalid external/internal parameters of the delay generator (delay time, cycle time, tics).',
    },
    17003: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"External parameters of the superimposed instruction are invalid" Invalid external parameters of the superimposed functionality (acceleration, deceleration, velocity, process velocity, length).',
    },
    17004: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid override type."',
    },
    17005: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Activation position under/overrun" The requested activation position is located in the past of the master (e.g. when exchanging a cam table).',
    },
    17006: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Activation impossible: Master is standing" The required activation of the correction is impossible since the master axis is not moving. A synchronization is not possible, because the master axis standing and the slave axis is still not synchronous.',
    },
    17007: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Activation mode not possible" The requested activation mode is not possible when the slave axis is moving. Otherwise the slave velocity would jump to zero.',
    },
    17008: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Start parameter for the compensation is invalid" One of the dynamic parameters for the compensation is invalid (necessary condition): Acceleration (>0) Deceleration (>0) Process velocity (>0)',
    },
    17009: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Start parameter for the compensation is invalid" Velocity camber is negative.',
    },
    17010: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Start parameter for the compensation is invalid" The section on which the compensation is to occur is not positive.',
    },
    17011: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Target position under/overrun" (INTERNAL ERROR) The position (calculated from the modulo-target-position) where the axis should stand at end of oriented stop has been run over.',
    },
    17012: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Target position will be under/overrun" (INTERNAL ERROR) The position (calculated from the modulo-target-position) where the axis should stand at end of oriented stop is too near and will be run over.',
    },
    17014: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"GROUPERR_GUIDERSTARTDATA"',
    },
    17015: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Dynamic parameters not permitted" (INTERNAL ERROR) The dynamic parameters resulting from internal calculation like acceleration, deceleration and jerk are not permitted.',
    },
    17017: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"GROUPERR_GUIDEROVERRUN"',
    },
    17018: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"GROUPERR_GUIDERLOOKAHEAD"',
    },
    17019: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"GROUPERR_GUIDERLOOKAHEADEND"',
    },
    17020: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"GROUPERR_GUIDERLOOKAHEADREQU"',
    },
    17021: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"GROUPERR_GUIDERMODE"',
    },
    17022: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"A requested motion command could not be realized (BISECTION)" A requested motion command could not be realized using the requested parameters. The command has been executed best possible and this message is therefore to be understood just as a warning. Samples: An axis motion command is requested while the axis is in a unfavorable dynamic situation (acceleration phase), in which the covered distance is too short or the velocity is clearly too high. Another possibility is a slave axis, which is decoupled in motion in an unfavorable dynamic situation and is afterwards given a motion as in the previous case.',
    },
    17023: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"The new target position either has been overrun or will be overrun" The new target position either has been overrun or will be overrun, since until there it is impossible to stop. An internal stop command is commended.',
    },
    17024: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Group not ready / group not ready for new task" (INTERNAL ERROR / INFORMATION) The group is being given a new task while it is still in the process of executing an existing task. This request is not allowed because it would interrupt the execution of the previous task. The new task could, for instance, be a positioning command, or the "set actual position" function. Precisely the converse relationships apply for the "set new end position" function. In that case, the group/axis must still be actively moving in order to be able to cause a change in the end position.',
    },
    17025: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"The parameters of the oriented stop (O-Stop) are not admitted." The modulo-target position should not be smaller than zero and not larger or equal than the encoder mod-period ( e.g. in the interval [0.0,360.0] ).Note: In the case of error the axis is safely stopped, but is afterwards not at the requested oriented position.',
    },
    17026: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"The modulo target position of the modulo-start is invalid" The modulo target position is outside of the valid parameter range. So the position value should not be smaller than zero and not greater or equal than the encoder modulo-period (e. g. in the interval [0.0,360.0] for the modulo start type "SHORTEST_WAY (261)" ).',
    },
    17027: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"The online change activation mode is invalid". The activation can be used with online scaling or with online modification of motion function. The used activation is invalid in this context. Either the mode is not defined or yet not implemented or however it cannot in this constellation be put into action (e.g. when linear tables are used with an unexpected cyclic activation mode NEXTCYCLE or NEXTCYCLEONCE). In some case, the activation mode may be valid but the command cannot be executed due to a pending previous command.',
    },
    17028: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"The parameterized jerk rate is not permitted". The jerk rate is smaller than the minimum jerk rate. The minimum value for jerk rate is 1.0 (e.g. mm/s^3).',
    },
    17029: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"The parameterized acceleration or deceleration is not permitted". The parameterized acceleration or deceleration is lower than the permitted minimum acceleration. The value for minimum acceleration is calculated from minimum jerk rate and NC cycle time (minimum jerk rate multiplied with NC cycle time). The unit for example is mm/s^2.',
    },
    17030: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"The parameterized velocity is not permitted". The parameterized target velocity is lower than the minimum velocity (but the value zero is permitted). The value for minimum velocity is calculated from the minimum jerk rate and the NC cycle time (minimum jerk rate multiplied with the square of the NC cycle time). The unit for example is mm/s.',
    },
    17031: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"A activation cannot be executed due to a pending activation" A activation e.g. "CamIn", "CamScaling" or "WriteMotionFunction" cannot be executed due to a pending activation (e.g. "CamIn", "CamScaling", "WriteMotionFunction"). Only activation can be enabled.',
    },
    17032: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Illegal combination of different cycle times within an axis group" A logical axis group includes elements (axes) with different cycle times for a common setpoint generator and I/O-execution, resp. This situation can occur with Master/Slave-coupling or configuring 3D- and FIFO-groups (including path, auxiliary, and slave axes).',
    },
    17033: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Illegal motion reversal" Due to the actual dynamical state a motion reversal will happen. To avoid this motion reversal the axis command is not performed and the previous system state restored.',
    },
    17034: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Illegal moment for an axis command because there is an old axis command with activation position still active" The moment for the command is illegal because there is still an old command with activation position active (e.g. "go to new velocity at threshold position" or "reach new velocity at threshold position").',
    },
    17035: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Error in the stop-calculation routine" (INTERNAL ERROR) Due to an internal error in the stop-calculation routine the current commando cannot be performed. The previous system state is restored.',
    },
    17036: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"A command with activation position cannot fully be performed because the remaining path is too short"A command with activation position (threshold) like "reach a new velocity at a position" can be just partially executed because the path from the actual position to the activation position is too short.',
    },
    17037: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Illegal decouple type when decoupling a slave axis" The decouple and restart command contains an invalid decouple type.',
    },
    17038: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Illegal target velocity when decoupling a slave axis" The decouple and restart command contains an illegal target velocity [1 < V <Vmax].',
    },
    17039: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"The command new dynamic parameter cannot be performed since this would require a new target velocity"Das Kommando zum Aktivieren neuer Dynamikparameter wie Beschleunigung, Verzögerung und Ruck kann nicht durchgeführt werden, da dies eine neue beauftragte Fahrgeschwindigkeit erfordern würde.This situation can occur, for example, if the axis is near the target position in an accelerated state and the dynamics parameter are chosen softer.',
    },
    17040: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"A command with activation position cannot be performed because the axis is already in the brake phase" A command with activation position (threshold) e.g. "reach new velocity at position" cannot be performed because the axis is already in the brake phase and the remaining path from the actual position to the activation position is too short.',
    },
    17041: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Decouple routine of slave axis doesn\'t return a valid solution" Internal jerk scaling of decouple routine cannot evaluate a valid solution (decoupling slave axis and transform to master axis). The command is rejected because velocity can become too high, a reversal of movement can occur, or the target position can be passed.',
    },
    17042: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Command not be executed because the command buffer is full filled" The command is rejected because the command buffer is full filled.',
    },
    17043: {
        "Category": "Group Errors",
        "Error type": "Internal",
        "Description": '"Command is rejected due to an internal error in the Look Ahead" (INTERNAL ERROR) The command is rejected due to an internal error in the "look ahead".',
    },
    17044: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Command is rejected because the segment target velocity is not realized" The command is rejected, because the new target segment velocity Vrequ is not realizable and an internal optimizing is impossible.',
    },
    17045: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Successive commands have the same final position" Successive commands have the same final position. So the moving distance is zero.',
    },
    17046: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Logical positioning direction is inconsistent with the direction of the buffer command" In the extended buffer mode, where the actual end position is replaced by the new buffer start position, the logical positioning direction is inconsistent with the direction of the buffer command (=> contradiction).\xa0A buffered command (BufferMode, BlendingLow, BlendingPrevious, BlendingNext, BlendingHigh) is rejected with error 0x4296 if the command is using the Beckhoff specific optional BlendingPosition but the blending position is located beyond the target position of the previous motion command.',
    },
    17047: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Command is rejected because the remaining positioning length is to small" The command is rejected because the remaining path length is too small. E.g. when the buffer mode is used and the remaining positioning length in the actual segment is too small for getting the axis in a force free state or to reach the new target velocity at the change of segment.',
    },
    17051: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": "„collect error for invalid start parameters“ This error refers to a wrong parameterization of the user (collect error). E. g. dynamic parameters like Velo, Acc or Dec could be equal or less than zero.Or following errors:- BaseFrequence < 0.0- StartFrequence < 1.0- StepCount < 1, StepCount > 200- BaseAmplitude <= 0.0- StepDuration <= 0.0- StopFrequence >= 1/(2*CycleTime)",
    },
    17052: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Reference cam is not found" During the referencing process for an axis it is moved in the direction of the referencing cam. This reference cam, however, was not found as expected (=> leads to the abortion of the referencing procedure).',
    },
    17053: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Reference cam became not free" During the referencing process for an axis it is moved in the direction of the referencing cam, and is only stopped again when the cam signal is reached. After the axis has also come to a physical standstill, the axis is subsequently started regularly from the cam again. In this case, the reference cam did not become free again as expected when driving down (=> leads to the abortion of the referencing procedure).',
    },
    17054: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"IO sync pulse was not found (only when using hardware latch)" If the hardware latch is activated, a sync pulse (zero pulse) is expected to be found and a sync event triggered following the expiry of a certain time or a certain distance. If this is not the case, the reaction is an error and the abortion of the referencing procedure.',
    },
    17056: {
        "Category": "Group Errors",
        "Error type": "Internal",
        "Description": '"Group/axis consequential error" Consequential error resulting from another causative error related to another axis within the group. Group/axis consequential errors can occur in relation to master/slave couplings or with multiple axis interpolating DXD groups. If, for instance, it is detected that the following error limit of a master axis has been exceeded, then this consequential error is assigned to all the other master axes and slave axes in this group.',
    },
    17057: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Velocity reduction factor for C0/C1 transition is not allowed" A C0 transition describes two geometries which, while they are themselves continuous, no not have either continuous first or second differentials. The velocity reduction factor C0 acts on such transitions. Note: A C1 transition is characterized by the two geometries being continuous, but having only a first differential that is continuous. The velocity reduction factor C1 acts on such transitions.',
    },
    17058: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Critical angle at segment transition not allowed"',
    },
    17059: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Radius of the tolerance sphere" is in an invalid rang',
    },
    17060: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": "Not implemented.",
    },
    17061: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Start type"',
    },
    17062: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": "Not implemented.",
    },
    17063: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Blending" with given parameters not possible',
    },
    17064: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": "Not implemented.",
    },
    17065: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Curve velocity reduction method not allowed" (INTERNAL ERROR) The curve velocity reduction method does not exist.',
    },
    17066: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Minimum velocity not allowed"  The minimum velocity that has been entered is less than 0.0.',
    },
    17067: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Power function input not allowed" (INTERNAL ERROR) The input parameters in the power_() function lead to an FPU exception.',
    },
    17068: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Dynamic change parameter not allowed" A parameter that controls alterations to the dynamics is invalid. Parameter: 1. Absolute motion dynamics change: All parameters must be strictly positive. 2. Relative reduction c_f: 0.0 < c_f <= 1.0',
    },
    17069: {
        "Category": "Group Errors",
        "Error type": "Memory",
        "Description": '"Memory allocation error" (INTERNAL ERROR)',
    },
    17070: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"The calculated end position differs from the end position in the nc instruction (internal error)."',
    },
    17071: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Calculate remaining chord length"  invalid value Value range: [0,1]',
    },
    17072: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Set value generator SVB active" Starting the set value generator (SVB, SAF) has been refused, since the SVB task is already active.',
    },
    17073: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"SVB parameter not allowed" (INTERNAL ERROR) A parameter related to the internal structure of the set value generator (SVB) results in logical errors and/or to an FPU exception. Affects these parameters: Minimum velocity (>0.0), TimeMode, ModeDyn, ModeGeo, StartType, DistanceToEnd, TBallRadius.',
    },
    17074: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Velocity reduction factor not allowed" A parameter that controls reduction of the velocity at segment transitions is invalid. Parameter: 1. Transitions with continuous first differential: VeloVertexFactorC1 2. Not once continuously differentiable transitions: VeloVertexFactorC0, CriticalVertexAngleLow, CriticalVertexAngleHigh.',
    },
    17075: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Helix is a circle" The helix has degenerated to a circle, and should be entered as such.',
    },
    17076: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Helix is a straight line" The helix has degenerated to a straight line, and should be entered as such.',
    },
    17077: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Guider parameter not allowed" One of the guider\'s parameters leads to logical errors and/or to an FPU exception.',
    },
    17078: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Invalid segment address" (INTERNAL ERROR) The geometry segment does not have a valid geometry structure address or does not have a valid dynamic structure address.',
    },
    17079: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Unparameterized generator" (INTERNAL ERROR) The SVB generator is not yet parameterized and is therefore unable to operate.',
    },
    17080: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Unparameterized table" (INTERNAL ERROR) The table has no information concerning the address of the corresponding dynamic generator.',
    },
    17082: {
        "Category": "Group Errors",
        "Error type": "Internal",
        "Description": '"The calculation of the arc length of the smoothed path failed (internal error)."',
    },
    17083: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"The radius of the tolerance ball is too small (smaller than 0.1 mm)."',
    },
    17084: {
        "Category": "Group Errors",
        "Error type": "Internal",
        "Description": "Error while calculating DXD-Software-Limit switches (internal error)",
    },
    17085: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"NC-Block violates software limit switches of the group" At least one path axis with active software limit monitoring has violated the limit switches. Therefore the geometric entry is denied with an error.',
    },
    17086: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"GROUPERR_DXD_SOFTENDCHECK"',
    },
    17087: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"GROUPERR_DXD_RTTG_VELOREFERENCE"',
    },
    17088: {
        "Category": "Group Errors",
        "Error type": "Internal",
        "Description": '"Interpolating group contains axes of an incorrect axis type" An interpolating 3D group may only contain continuously guided axes of axis type 1 (SERVO).',
    },
    17089: {
        "Category": "Group Errors",
        "Error type": "Internal",
        "Description": '"Scalar product cannot be calculated" The length of one of the given vectors is 0.0.',
    },
    17090: {
        "Category": "Group Errors",
        "Error type": "Internal",
        "Description": '"Inverse cosine cannot be calculated" The length of one of the given vectors is 0.0.',
    },
    17091: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid table entry type" The given table entry type is unknown.',
    },
    17092: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid DIN66025 information type" (INTERNAL ERROR) The given DIN66025 information type is unknown. Known types: G0, G1, G2, G3, G17, G18, G19.',
    },
    17093: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid dimension" (INTERNAL ERROR) The CNC dimension is unknown. Known dimensions: 1, 2, 3. Or: The CNC dimension is invalid for the given geometrical object. For a circle the dimension must be 2 or 3, while for a helix it must be 3.',
    },
    17094: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Geometrical object is not a straight line" The given object, interpreted as a straight line, has a length of 0.0.',
    },
    17095: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Geometrical object is not a circle" Interpreted as a circular arc, the given object has a length of 0.0, or an angle of 0.0 or a radius of 0.0.',
    },
    17096: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Geometrical object is not a helix" Interpreted as a circular arc, the given object has a length of 0.0, or an angle of 0.0, or a radius of 0.0. or a height of 0.0.',
    },
    17097: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Set velocity less than or equal to 0.0 is invalid" A value less than or equal to 0.0 for the set velocity (CNC) is not allowed, since the set velocity is positive by definition, and a set velocity of 0.0 cannot generate any motion.',
    },
    17098: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Address for look-ahead invalid" (INTERNAL ERROR) The address supplied for the look-ahead is invalid.',
    },
    17099: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Set value generator SAF active" Starting the set value generator (SAF) has been refused, since the SAF task is already active.',
    },
    17100: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"CNC set value generation not active" Stop or change of override refused, because the set value generation is not active.',
    },
    17101: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"CNC set value generation in the stop phase" Stop or change of override refused, because the set value generation is in the stop phase.',
    },
    17102: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Override not allowed" An override of less than 0.0 % or more than 100.0 % is invalid.',
    },
    17103: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"Invalid table address" (INTERNAL ERROR) The table address given for the initialization of the set value generator is invalid, or no valid logger connection (report file) is present.',
    },
    17104: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid table entry type" The given table entry type is unknown.',
    },
    17105: {
        "Category": "Group Errors",
        "Error type": "Memory",
        "Description": '"Memory allocation failed" Memory allocation for the table has failed.',
    },
    17106: {
        "Category": "Group Errors",
        "Error type": "Memory",
        "Description": '"Memory allocation failed" Memory allocation for the filter has failed.',
    },
    17107: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid parameter" Filter parameter is not allowed.',
    },
    17108: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": "\"Delete Distance To Go failed\" Delete Distance to go (only interpolation) failed. This error occurred, if e.g. the command 'DelDTG' was not programmed in the actual movement of the nc program.",
    },
    17109: {
        "Category": "Group Errors",
        "Error type": "Internal",
        "Description": '"The setpoint generator of the flying saw generates incompatible values (internal error)"',
    },
    17110: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Axis will be stopped since otherwise it will overrun its target position (old PTP setpoint generator)" If, for example, in case of a slave to master transformation for the new master a target position is commanded that will be overrun because of the actual dynamics the axis will be stopped internally to guarantee that the target position will not be overrun.',
    },
    17111: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Internal error in the transformation from slave to master."',
    },
    17112: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Wrong direction in the transformation of slave to master."',
    },
    17114: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Parameter of Motion Function (MF) table incorrect" The parameter of the Motion Function (MF) are invalid. This may refer to the first time created data set or to online changed data.',
    },
    17115: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Parameter of Motion Function (MF) table incorrect" The parameter of the Motion Function (MF) are invalid. This may refer to the first time created data set or to online changed data. The error cause can be, that an active MF point (no IGNORE point) points at a passive MF point (IGNORE point).',
    },
    17116: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Internal error by using Motion Function (MF)" An internal error occurs by using the Function (MF). This error cannot be solved by the user. Please ask the TwinCAT Support.',
    },
    17117: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Axis coupling with synchronization generator declined because of incorrect axis dynamic values" The axis coupling with the synchronization generator has been declined, because one of the slave dynamic parameter (machine data) is incorrect. Either the maximum velocity, the acceleration, the deceleration or the jerk is smaller or equal to zero, or the expected synchronous velocity of the slave axis is higher as the maximum allowed slave velocity.',
    },
    17118: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"Coupling conditions of synchronization generator incorrect" During positive motion of the master axis it has to be considered, that the master synchronous position is larger than the master coupling position ("to be in the future"). During negative motion of the master axis it has to be considered that the master synchronous position is smaller than the master coupling position.',
    },
    17119: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Moving profile of synchronization generator declines dynamic limit of slave axis or required characteristic of profile" One of the parameterized checks has recognized an overstepping of the dynamic limits (max. velocity, max. acceleration, max. deceleration or max. jerk) of the slave axis, or an profile characteristic (e.g. overshoot or undershoot in the position or velocity) is incorrect. See also further messages in the windows event log and in the message window of the System Manager.',
    },
    17120: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid parameter" The encoder generator parameter is not allowed.',
    },
    17121: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid parameter" The external (Fifo) generator parameter is not allowed.',
    },
    17122: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"External generator is active" The external generator cannot be started, as it is already active.',
    },
    17123: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"External generator is not active" The external generator cannot be stopped, as it is not active.',
    },
    17124: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"NC-Block with auxiliary axis violates software limit switches of the group" At least one auxiliary axis with active software limit monitoring has violated the limit switches. Therefore the geometric entry is denied with an error.',
    },
    17125: {
        "Category": "Group Errors",
        "Error type": "Function",
        "Description": '"NC-Block type Bezier spline curve contains a cusp (singularity)" The Bezier spline curve contain a cusp, i.e. at a certain interior point both the curvature and the modulus of the velocity tend to 0 such that the radius of curvature is infinite. Note: Split the Bezier curve at that point into two Bezier spline curves according to the de "Casteljau algorithm". This preserves the geometry and eliminates the interior singularity.',
    },
    17127: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Value for dead time compensation not allowed" The value for the dead time compensation in seconds for a slave coupling to an encoder axis (virtual axis) is not allowed.',
    },
    17128: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"GROUPERR_RANGE_NOMOTIONWINDOW"',
    },
    17129: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"GROUPERR_RANGE_NOMOTIONFILTERTIME"',
    },
    17130: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"GROUPERR_RANGE_TIMEUNITFIFO"',
    },
    17131: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"GROUPERR_RANGE_OVERRIDETYPE"',
    },
    17132: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"GROUPERR_RANGE_OVERRIDECHANGETIME"',
    },
    17133: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"GROUPERR_FIFO_INVALIDDIMENSION" Note: Since TC 2.11 Build 1547 the FIFO-dimension (number of axes) has been increased from 8 to 16.',
    },
    17134: {
        "Category": "Group Errors",
        "Error type": "Address",
        "Description": '"GROUPERR_ADDR_FIFOTABLE"',
    },
    17135: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"Axis is locked for motion commands because a stop command is still active" The axis/group is locked for motion commands because a stop command is still active. The axis can be released by calling MC_Stop with Execute=FALSE or by using MC_Reset (TcMC2.Lib).',
    },
    17136: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid number of auxiliary axes" The local number of auxiliary axes does not tally with the global number of auxiliary axes.',
    },
    17137: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid reduction parameter for auxiliary axes" The velocity reduction parameters for the auxiliary axes are inconsistent.',
    },
    17138: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid dynamic parameter for auxiliary axes" The dynamic parameters for the auxiliary axes are inconsistent.',
    },
    17139: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid coupling parameter for auxiliary axes" The coupling parameters for the auxiliary axes are inconsistent.',
    },
    17140: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid auxiliary axis entry" The auxiliary axis entry is empty (no axis motion).',
    },
    17142: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Invalid parameter" The limit for velocity reduction of the auxiliary axes is invalid. It has to be in the interval 0..1.0',
    },
    17144: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Block search - segment not found" The segment specified as a parameter could not be found by the end of the NC program.Possible cause:▪nBlockId is not specified in the mode described by eBlockSearchMode',
    },
    17145: {
        "Category": "Group Errors",
        "Error type": "Parameter",
        "Description": '"Blocksearch – invalid remaining segment length" The remaining travel in the parameter fLength is incorrectly parameterized',
    },
    17147: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": '"INTERNAL ERROR" (GROUPERR_SLAVE_INTERNAL)',
    },
    17151: {
        "Category": "Group Errors",
        "Error type": "Monitoring",
        "Description": "„GROUPERR_WATCHDOG“ (Customer specific error code)",
    },
    19456: {
        "Category": "Kinematic transformation",
        "Error type": "",
        "Description": "Transformation failed.",
    },
    19457: {
        "Category": "Kinematic transformation",
        "Error type": "",
        "Description": "Ambiguous answer. The answer of the transformation is not explicit.",
    },
    19458: {
        "Category": "Kinematic transformation",
        "Error type": "",
        "Description": "Invalid axis position: The transformation can not be calculated with the current position data. Possible causes:▪The position is outside the working area of the kinematics",
    },
    19459: {
        "Category": "Kinematic transformation",
        "Error type": "Configuration",
        "Description": "Invalid dimension: The dimension of the paramerterized input parameter does not match the dimension expected by the kinematic object.Possible causes:▪Too many position values are supplied for this configuration. Check the number of parameterized axes.",
    },
    19460: {
        "Category": "Kinematic transformation",
        "Error type": "",
        "Description": "NCERR_KINTRAFO_REGISTRATION",
    },
    19461: {
        "Category": "Kinematic transformation",
        "Error type": "Internal",
        "Description": "Newton iteration failed: The Newton iteration does not converge.",
    },
    19462: {
        "Category": "Kinematic transformation",
        "Error type": "Internal",
        "Description": "Jacobi matrix cannot be inverted",
    },
    19463: {
        "Category": "Kinematic transformation",
        "Error type": "Configuration",
        "Description": "Invalid cascade: This kinematic configuration is not permitted.",
    },
    19464: {
        "Category": "Kinematic transformation",
        "Error type": "Programming",
        "Description": "Singularity: The machine configuration results in singular axis velocities.",
    },
    19467: {
        "Category": "Kinematic transformation",
        "Error type": "Internal",
        "Description": "No metainfo: Metainfo pointer is null.",
    },
    19488: {
        "Category": "Kinematic transformation",
        "Error type": "Internal",
        "Description": "Transformation failed: Call of extended kinematic model failed.",
    },
    19504: {
        "Category": "Kinematic transformation",
        "Error type": "Programming",
        "Description": "Invalid input frame: Programmed Cartesian position cannot be reached in the ACS configuration.",
    },
    19536: {
        "Category": "Kinematic transformation",
        "Error type": "Internal",
        "Description": "Invalid offset: Access violation detected in the observer.",
    },
    17920: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": '‘"Drive ID not allowed" The value for the drive ID is not allowed, e.g. because it has already been assigned, is less than or equal to zero, or is greater than 255.',
    },
    17921: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Drive type impermissible’ The value for the drive type is impermissible, since it is not defined.",
    },
    17922: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Drive operating mode impermissible’ The value for the drive operating mode is impermissible (mode 1: standard).",
    },
    17923: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": '"Motor polarity inverted?" The flag for the motor polarity is not allowed. Flag 0: Positive motor polarity flag 1: Negative motor polarity',
    },
    17924: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Drift compensation/speed offset (DAC offset)’ The value for the drift compensation (DAC offset) is impermissible.",
    },
    17925: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Reference speed (velocity pre-control)’ The value for the reference speed (also called velocity pilot control) is impermissible.",
    },
    17926: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Reference output in percent’ The value for the reference output in percent is impermissible. The value 1.0 (100 %) usually corresponds to a voltage of 10.0 V.",
    },
    17927: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Quadrant compensation factor’ The value for the quadrant compensation factor is impermissible.",
    },
    17928: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Velocity reference point’ The value for the velocity reference point in percent is impermissible. The value 1.0 corresponds to 100 percent.",
    },
    17929: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Output reference point’ The value for the output reference point in percent is impermissible. The value 1.0 corresponds to 100 percent.",
    },
    17930: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Minimum or maximum output limits (output limitation)’ The value for the minimum and/or maximum output limit is impermissible. This will happen if the range of values is exceeded, the maximum limit is smaller than the minimum limit, or the distance between the minimum and maximum limits is zero. The minimum limit is initially set to –1.0 (-100 percent) and the maximum limit to 1.0 (100 percent).",
    },
    17931: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "“DRIVEERR_RANGE_MAXINCREMENT”",
    },
    17932: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "“DRIVEERR_RANGE_ DRIVECONTROLDWORD”",
    },
    17933: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "“DRIVEERR_RANGE_ RESETCYCLECOUNTER”",
    },
    17935: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Drive torque output scaling impermissible’ The value is impermissible as drive torque output scaling (rotary motor) or as force output scaling (linear motor).",
    },
    17936: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "„Drive velocity output scaling is not allowed“ The value for the drive velocity output scaling is not allowed.",
    },
    17937: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Profi Drive DSC proportional gain Kpc (controller) impermissible’ Positions The value for the Profi Drive DSC position control gain (Kpc factor) is impermissible.",
    },
    17938: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Table ID is impermissible’ The value for the table ID is impermissible.",
    },
    17939: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Table interpolation type is impermissible’ The value is impermissible as the table interpolation type.",
    },
    17940: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Output offset in percent is impermissible’ The value is impermissible as an output offset in percent (+/- 1.0).",
    },
    17941: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Profi Drive DSC scaling for calculation of “Xerr” (controller) impermissible’ Positions: the value is impermissible as Profi Drive DSC scaling for the calculation of ‘Xerr’.",
    },
    17942: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Drive acceleration output scaling impermissible’ The value is impermissible as drive acceleration/deceleration output scaling.",
    },
    17943: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Drive position output scaling impermissible’ The value is impermissible as drive position output scaling.",
    },
    17948: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Drive filter type impermissible for command variable filter for the output position’ The value is impermissible as a drive filter type for the smoothing of the output position (command variable filter for the setpoint position).",
    },
    17949: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Drive filter time impermissible for command variable filter for the output position’ The value is impermissible as a drive filter time for the smoothing of the output position (command variable filter for the setpoint position).",
    },
    17950: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Drive filter order impermissible for command variable filter for the output position’ The value is impermissible as a drive filter order (P-Tn) for the smoothing of the output position (command variable filter for the setpoint position).",
    },
    17952: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Bit mask for stepper motor cycle impermissible’ A value of the different stepper motor masks is impermissible for the respective cycle.",
    },
    17953: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Bit mask for stepper motor holding current impermissible’ The value for the stepper motor holding mask is impermissible.",
    },
    17954: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Scaling factor for actual torque (actual current) impermissible’ The value is impermissible as a scaling factor for the actual torque (or actual current).",
    },
    17955: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Filter time for actual torque is impermissible’ The value is impermissible as a filter time for the actual torque (or the actual current) (P-T1 filter).",
    },
    17956: {
        "Category": "Drive Errors",
        "Error type": "Parameter",
        "Description": "‘Filter time for the temporal derivation of the actual torque is impermissible’ The value is impermissible as a filter time for the temporal derivation of the actual torque (or actual current (P-T1 filter).",
    },
    17959: {
        "Category": "Drive Errors",
        "Error type": "Function",
        "Description": "DRIVEOPERATIONMODEBUSY. The activation of the drive operation mode failed, because another object with OID ... is already using this interface.",
    },
    17968: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "‘Overtemperature’ Overtemperature was detected or reported in the drive or terminal.",
    },
    17969: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "‘Undervoltage’ Undervoltage was detected or reported in the drive or terminal.",
    },
    17970: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "‘Wire break in phase A’ A wire break in phase A was detected or reported in the drive or terminal.",
    },
    17971: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "‘Wire break in phase B’ A wire break in phase B was detected or reported in the drive or terminal.",
    },
    17972: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "‘Overcurrent in phase A’ Overcurrent was detected or reported in phase A in the drive or terminal.",
    },
    17973: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "‘Overcurrent in phase B’ Overcurrent was detected or reported in phase B in the drive or terminal.",
    },
    17974: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "‘Torque overload (stall)’ A torque overload (stall) was detected or reported in the drive or terminal.",
    },
    17984: {
        "Category": "Drive Errors",
        "Error type": "Initialization",
        "Description": "‘Drive initialization’ Drive has not been initialized. Although the drive has been created, the rest of the initialization has not been performed (1. Initialization of drive I/O, 2. Initialization of drive, 3. Reset drive).",
    },
    17985: {
        "Category": "Drive Errors",
        "Error type": "Address",
        "Description": "‘Axis address’ Drive does not know its axis, or the axis address has not been initialized.",
    },
    17986: {
        "Category": "Drive Errors",
        "Error type": "Address",
        "Description": "‘Address IO input structure’ Drive has no valid IO input address in the process image.",
    },
    17987: {
        "Category": "Drive Errors",
        "Error type": "Address",
        "Description": "‘Address IO output structure’ Drive has no valid IO output address in the process image.",
    },
    18000: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": '‘Drive hardware not ready to operate’  The drive hardware is not ready for operation. The following are possible causes: - the drive is in the error state (hardware error) - the drive is in the start-up phase (e.g. after an axis reset that was preceded by a hardware error) - the drive is missing the controller enable (ENABLE) Note: The time required for "booting" a drive after a hardware fault can amount to several seconds.',
    },
    18001: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "Error in the cyclic communication of the drive (Life Counter). Reasons for this could be an interrupted fieldbus or a drive that is in the error state.",
    },
    18002: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "‘Changing the table ID when active controller enable is impermissible’. Changing (deselecting, selecting) the characteristic curve table ID is not permissible when the controller enable for the axis is active.",
    },
    18005: {
        "Category": "Drive Errors",
        "Error type": "Monitoring",
        "Description": "‘Invalid IO data for more than ‘n’ continuous NC cycles’ The axis (encoder or drive) has detected invalid IO data (e.g. n=3) for more than ‘n’ continuous NC cycles (NC SAF task). EtherCAT fieldbus: ‘working counter error ('WCState')’As a result it is possible that the encoder referencing flag will be reset to FALSE (i.e. the encoder is given the status ‘unreferenced’). Lightbus fieldbus: ‘CDL state error ('CdlState')’As a result it is possible that the encoder calibration flag will set to FALSE (that means uncalibrated).",
    },
    16641: {
        "Category": "Channel Errors",
        "Error type": "Parameter",
        "Description": '"Group index not allowed" The location within the channel specified for a group is not allowed.',
    },
    16642: {
        "Category": "Channel Errors",
        "Error type": "Address",
        "Description": '"Null pointer" The pointer to the group is invalid. This is usually a consequence of an error at system start-up.',
    },
    16643: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": '"No process image" It is not possible to exchange data with the PLC. Possible causes: n the channel does not have an interface (no interpreter present) n The connection to the PLC is faulty',
    },
    16644: {
        "Category": "Channel Errors",
        "Error type": "Parameter",
        "Description": '"M-function index not allowed" Unacceptable M-function (not 0...159) detected at the execution level.',
    },
    16645: {
        "Category": "Channel Errors",
        "Error type": "Memory",
        "Description": '"No memory" No more system memory is available. This is usually the result of another error.',
    },
    16646: {
        "Category": "Channel Errors",
        "Error type": "Function",
        "Description": '"Not ready" The function is not presently available, because a similar function is already being processed. This is usually the result of access conflicts: more than one instance wants to issue commands to the channel. This can, for example, be the consequence of an incorrect PLC program.',
    },
    16647: {
        "Category": "Channel Errors",
        "Error type": "Function",
        "Description": '"Function/command not supported" A requested function or command is not supported by the channel.',
    },
    16648: {
        "Category": "Channel Errors",
        "Error type": "Parameter",
        "Description": '"Invalid parameter while starting" Parameters to start the channel (TwinCAT-Start) are invalid. Typically there is an invalid memory size or channel type requested.',
    },
    16649: {
        "Category": "Channel Errors",
        "Error type": "Function",
        "Description": '"Channel function/command not executable" A channel function e.g. interpreter start is not executable because the channel is already busy, no program is loaded or in an error state.',
    },
    16650: {
        "Category": "Channel Errors",
        "Error type": "Function",
        "Description": '"ItpGoAhead not executable" The requested command is not executable, because the interpreter is not executing a decoder stop.',
    },
    16656: {
        "Category": "Channel Errors",
        "Error type": "Parameter",
        "Description": '"Error opening a file" The specified file does not exist. Sample: NC program unknown.',
    },
    16657: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Syntax error during loading" The NC has found a syntax error when loading an NC program.',
    },
    16658: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Syntax error during interpretation" The NC has found a syntax error when executing an NC program.',
    },
    16659: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Missing subroutine" The NC has found a missing subroutine while loading.',
    },
    16660: {
        "Category": "Channel Errors",
        "Error type": "Memory",
        "Description": '"Loading buffer of interpreter is too small" The capacity of the interpreter loading buffer has been exceeded.',
    },
    16661: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": "“Symbolic” - reserved",
    },
    16662: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": "“Symbolic” - reserved",
    },
    16663: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Subroutine incomplete" Header of subroutine is missing',
    },
    16664: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Error while loading the NC program" The maximum number of loadable NC programs has been reached.Possible cause:Too many sub-programs were loaded from a main program.',
    },
    16665: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Error while loading the NC program" The program name is too long.',
    },
    16672: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Divide by zero" The NC encountered a computation error during execution: division by 0.',
    },
    16673: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Invalid circle parameterization" The NC encountered a computation error during execution: The specified circle cannot be calculated.',
    },
    16674: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Invalid FPU-Operation" The NC encountered an invalid FPU-Operation during execution. This error occurs e.g. by calculating the square root of a negative number.',
    },
    16688: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Stack overflow: subroutines" The NC encountered a stack overflow during execution: too many subroutine levels.',
    },
    16689: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Stack underflow: subroutines" The NC encountered a stack underflow during execution: too many subroutine return commands. Note: A main program must not end with a return command.',
    },
    16690: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Stack overflow: arithmetic unit" The NC encountered a stack overflow during execution: The calculation is too complex, or has not been correctly written.',
    },
    16691: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Stack underflow: arithmetic unit" The NC encountered a stack underflow during execution: The calculation is too complex, or has not been correctly written.',
    },
    16704: {
        "Category": "Channel Errors",
        "Error type": "Parameter",
        "Description": '"Register index not allowed" The NC encountered an unacceptable register index during execution: Either the program contains an unacceptable value (not R0...R999) or a pointer register contains an unacceptable value.',
    },
    16705: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Unacceptable G-function index" The NC has encountered an unacceptable G-function (not 0...159) during execution.',
    },
    16706: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Unacceptable M-function index" The NC has encountered an unacceptable M-function (not 0...159) during execution.',
    },
    16707: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Unacceptable extended address" The NC has encountered an unacceptable extended address (not 1...9) during execution.',
    },
    16708: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Unacceptable index to the internal H-function" The NC has encountered an unacceptable internal H-function in the course of processing. This is usually a consequence of an error during loading.',
    },
    16709: {
        "Category": "Channel Errors",
        "Error type": "Parameter",
        "Description": '"Machine data value unacceptable" While processing instructions the NC has detected an impermissible value for the machine data (MDB) (not 0…7).',
    },
    16720: {
        "Category": "Channel Errors",
        "Error type": "Parameter",
        "Description": '"Cannot change tool params here" The NC has encountered an unacceptable change of parameters for the tool compensation during execution. This error occurred for instance by changing the tool radius and programming a circle in the same block.',
    },
    16721: {
        "Category": "Channel Errors",
        "Error type": "Parameter",
        "Description": '"Cannot calculate tool compensation" The NC has encountered an error by the calculation of the tool compensation.',
    },
    16722: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": "Tool compensation: The plane for the tool compensation cannot be changed here. This error occurred for instance by changing the tool plane when the compensation is turned on or active.",
    },
    16723: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": "Tool compensation: The D-Word is missing or invalid by turning on the tool compensation.",
    },
    16724: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": "Tool compensation: The specified tool radius is invalid because the value is less or equal zero.",
    },
    16725: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": "Tool compensation: The tool radius cannot be changed here",
    },
    16726: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": "Tool compensation: Collision Detection Table is full.",
    },
    16727: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": "Tool compensation: Internal error while turning on the contour collision detection.",
    },
    16728: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": "Tool compensation: Internal error within the contour collision detection: update reversed geo failed.",
    },
    16729: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": "Tool compensation: Unexpected combination of geometry types by active contour collision detection.",
    },
    16730: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": "Tool compensation: Programmed inner circle is smaller than the cutter radius",
    },
    16731: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": "Tool compensation: Bottle neck detection recognized contour violation",
    },
    16732: {
        "Category": "Channel Errors",
        "Error type": "Memory",
        "Description": "Table for corrected entries is full",
    },
    16733: {
        "Category": "Channel Errors",
        "Error type": "Memory",
        "Description": "Input table for tangential following is full",
    },
    16734: {
        "Category": "Channel Errors",
        "Error type": "Memory",
        "Description": "Executing table for tangential following is full",
    },
    16735: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": "Geometric entry for tangential following cannot be calculated",
    },
    16736: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": "reserved",
    },
    16737: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": "reserved",
    },
    16738: {
        "Category": "Channel Errors",
        "Error type": "Parameter",
        "Description": "The actual active interpolation rules (g-code), zero-shifts, or rotation cannot be detected",
    },
    16752: {
        "Category": "Channel Errors",
        "Error type": "NC programming",
        "Description": '"Error while loading: Invalid parameter" The NC has found an invalid parameter while loading an NC program.',
    },
    16753: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": '"Invalid contour start position" The NC encountered a computation error during execution: The specified contour cannot be calculated because the initial position is not on the contour.',
    },
    16754: {
        "Category": "Channel Errors",
        "Error type": "Internal",
        "Description": '"Retrace: Invalid internal entry index" The NC encountered an invalid internal entry index during execution of the retrace function.',
    },
    33024: {
        "Category": "Bode Return Codes",
        "Error type": "INTERNAL",
        "Description": "Internal error",
    },
    33025: {
        "Category": "Bode Return Codes",
        "Error type": "NOTINITIALIZED",
        "Description": "Not initialized (e.g. no nc axis)",
    },
    33026: {
        "Category": "Bode Return Codes",
        "Error type": "INVALIDPARAM",
        "Description": "Invalid parameter",
    },
    33027: {
        "Category": "Bode Return Codes",
        "Error type": "INVALIDOFFSET",
        "Description": "Invalid index offset",
    },
    33028: {
        "Category": "Bode Return Codes",
        "Error type": "INVALIDSIZE",
        "Description": "Invalid parameter size",
    },
    33029: {
        "Category": "Bode Return Codes",
        "Error type": "INVALIDSTARTPARAM",
        "Description": "Invalid start parameter (set point generator)",
    },
    33030: {
        "Category": "Bode Return Codes",
        "Error type": "NOTSUPPORTED",
        "Description": "Not supported",
    },
    33031: {
        "Category": "Bode Return Codes",
        "Error type": "AXISNOTENABLED",
        "Description": "Nc axis not enabled",
    },
    33032: {
        "Category": "Bode Return Codes",
        "Error type": "AXISINERRORSTATE",
        "Description": "Nc axis in error state",
    },
    33033: {
        "Category": "Bode Return Codes",
        "Error type": "DRIVEINERRORSTATE",
        "Description": "IO drive in error state",
    },
    33034: {
        "Category": "Bode Return Codes",
        "Error type": "AXISANDDRIVEINERROR-STATE",
        "Description": "Nc axis AND IO drive in error state",
    },
    33035: {
        "Category": "Bode Return Codes",
        "Error type": "INVALIDDRIVEOPMODE",
        "Description": "Invalid drive operation mode active or requested (no bode plot mode)",
    },
    33036: {
        "Category": "Bode Return Codes",
        "Error type": "INVALIDCONTEXT",
        "Description": "Invalid context for this command (mandatory task or windows context needed)",
    },
    33037: {
        "Category": "Bode Return Codes",
        "Error type": "NOAXISINTERFACE",
        "Description": "Missing TCom axis interface (axis null pointer).There is no connection to the NC axis.Either no axis (or axis ID) has been parameterized, or the parameterized axis does not exist.",
    },
    33038: {
        "Category": "Bode Return Codes",
        "Error type": "INPUTCYCLECOUNTER",
        "Description": 'Invalid input cycle counter from IO drive (e.g. frozen).The cyclic drive data are backed up by an ‘InputCycleCounter’ during the bode plot recording. This allows firstly the detection of an unexpected communication loss (keyword: LifeCounter) and secondly a check for temporal data consistency to be performed.Sample 1: This error can occur if the cycle time of the calling task is larger than the assumed drive cycle time (in this case, however, the error occurs right at the start of the recording).Sample 2: This error can occur if the calling task has real-time errors (e.g. the "Exceed Counter" of the task increments or the task has a lower priority, as is often the case, for example, with the PLC). In this case the error can also occur at any time during the recording.Sample 3: This error can occur more frequently if the real-time load on the computer is quite high (>50\xa0%).Note: Refer also to the corresponding AX5000 drive error code F440.',
    },
    33039: {
        "Category": "Bode Return Codes",
        "Error type": "POSITIONMONITORING(=> NC Runtime Error)",
        "Description": "Position monitoring: Axis position is outside of the maximum allowed moving range.The axis has left the parameterized position range window, whereupon the recording was aborted and the NC axis was placed in the error state 0x810F (with standard NC error handling).The position range window acts symmetrically around the initial position of the axis (see also parameter description Position Monitoring Window).Typical error message in the logger:\"BodePlot: 'Position Monitoring' error 0x%x because the actual position %f is above the maximum limit %f of the allowed position range (StartPos=%f, Window=%f)\"",
    },
    33040: {
        "Category": "Bode Return Codes",
        "Error type": "DRIVELIMITATIONDETECTED",
        "Description": 'Driver limitations detected (current or velocity limitations) which causes a nonlinear behavior and invalid results of the bode plot.A bode plot recording requires an approximately linear transmission link. If the speed or current is limited in the drive unit, however, this non-linear behavior is detected and the bode plot recording is aborted. Reasons for these limitations can be: choosing too large an amplitude for the position, speed or torque interface, or an unsuitable choice of amplitude scaling mode (see also parameter description Amplitude Scaling Mode, Base Amplitude, Signal Amplitude).Typical error message in the logger:"BodePlot: Sequence aborted with error 0x%x because the current limit of the drive has been exceeded (%d times) which causes a nonlinear behavior and invalid results of the bode plot"',
    },
    33041: {
        "Category": "Bode Return Codes",
        "Error type": "LIFECOUNTERMONITORING(=> NC Runtime Error)",
        "Description": "Life counter monitoring (heartbeat): Lost of communication to GUI detected after watchdog timeout is elapsed.The graphical user interface from which the bode plot recording was started is no longer communicating with the bode plot driver in the expected rhythm (keyword: ‘Life Counter’). Therefore the recording is terminated immediately and the NC axes are placed in the error state 0x8111 (with standard NC error handling). Possible reasons for this can be an operating interface crash or a major malfunction of the Windows context.Typical error message in the logger:\"BodePlot: Sequence aborted with GUI Life Counter error 0x%x because the WatchDog timeout of %f s elapsed ('%s')\"",
    },
    33042: {
        "Category": "Bode Return Codes",
        "Error type": "NCERR_BODEPLOT_WCSTATE",
        "Description": "WC state error (IO data working counter)IO working counter error (WC state), for example due to real-time errors, EtherCAT CRC errors or telegram failures, EtherCAT device not communicating (OP state), etc.",
    },
    33043: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33044: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33045: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33046: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33047: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33048: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33049: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33050: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33051: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33052: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33053: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33054: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    33055: {
        "Category": "Bode Return Codes",
        "Error type": "RESERVED",
        "Description": "Reserved area",
    },
    17152: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Axis ID not allowed" The value for the axis ID is not allowed, e.g. because it has already been assigned, is less than or equal to zero, is greater than 255, or does not exist in the current configuration.',
    },
    17153: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Axis type not allowed" The value for the axis type is unacceptable because it is not defined. Type 1: Servo Type 2: Fast/creep Type 3: Stepper motor',
    },
    17158: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Slow manual velocity not allowed" The value for the slow manual velocity is not allowed.',
    },
    17159: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Fast manual velocity not allowed" The value for the fast manual velocity is not allowed.',
    },
    17160: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"High speed not allowed" The value for the high speed is not allowed.',
    },
    17161: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Acceleration not allowed" The value for the axis acceleration is not allowed.',
    },
    17162: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Deceleration not allowed" The value for the axis deceleration is not allowed.',
    },
    17163: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Jerk not allowed" The value for the axis jerk is not allowed.',
    },
    17164: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Delay time between position and velocity is not allowed" The value for the delay time between position and velocity ("idle time compensation") is not allowed.',
    },
    17165: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Override-Type not allowed" The value for the velocity override type is not allowed. Type 1: With respect to the internal reduced velocity (default value) Type 2: With respect to the original external start velocity',
    },
    17166: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"NCI: Velo-Jump-Factor not allowed"  The value for the velo-jump-factor ("VeloJumpFactor") is not allowed. This parameter only works for TwinCAT NCI.',
    },
    17167: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"NCI: Radius of tolerance sphere for the auxiliary axes is invalid"  It was tried to enter an invalid value for the size of the tolerance sphere. This sphere affects only auxiliary axes!',
    },
    17168: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"NCI: Value for maximum deviation for the auxiliary axes is invalid"  It was tried to enter an invalid value for the maximum allowed deviation. This parameter affects only auxiliary axes!',
    },
    17170: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Referencing velocity in direction of cam not allowed" The value for the referencing velocity in the direction of the referencing cam is not allowed.',
    },
    17171: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Referencing velocity in sync direction not allowed" The value for the referencing velocity in the direction of the sync pulse (zero track) is not allowed.',
    },
    17172: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Pulse width in positive direction not allowed" The value for the pulse width in the positive direction is not allowed (pulsed operation). The use of the pulse width for positioning is chosen implicitly through the axis start type. Pulsed operation corresponds to positioning with a relative displacement that corresponds precisely to the pulse width.',
    },
    17173: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Pulse width in negative direction not allowed" The value for the pulse width in the negative direction is not allowed (pulsed operation). The use of the pulse width for positioning is chosen implicitly through the axis start type. Pulsed operation corresponds to positioning with a relative displacement that corresponds precisely to the pulse width.',
    },
    17174: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Pulse time in positive direction not allowed" The value for the pulse width in the positive direction is not allowed (pulsed operation).',
    },
    17175: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Pulse time in negative direction not allowed" The value for the pulse width in the negative direction is not allowed (pulsed operation).',
    },
    17176: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Creep distance in positive direction not allowed" The value for the creep distance in the positive direction is not allowed.',
    },
    17177: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Creep distance in negative direction not allowed" The value for the creep distance in the negative direction is not allowed.',
    },
    17178: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Braking distance in positive direction not allowed" The value for the braking distance in the positive direction is not allowed.',
    },
    17179: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Braking distance in negative direction not allowed" The value for the braking distance in the negative direction is not allowed.',
    },
    17180: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Braking time in positive direction not allowed" The value for the braking time in the positive direction is not allowed.',
    },
    17181: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Braking time in negative direction not allowed" The value for the braking time in the negative direction is not allowed.',
    },
    17182: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Switching time from high to low speed not allowed" The value for the time to switch from high to low speed is not allowed.',
    },
    17183: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Creep distance for stop not allowed" The value for the creep distance for an explicit stop is not allowed.',
    },
    17184: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Motion monitoring not allowed" The value for the activation of the motion monitoring is not allowed.',
    },
    17185: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Position window monitoring not allowed" The value for the activation of the position window monitoring is not allowed.',
    },
    17186: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Target window monitoring not allowed" The value for the activation of target window monitoring is not allowed.',
    },
    17187: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Loop not allowed" The value for the activation of loop movement is not allowed.',
    },
    17188: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Motion monitoring time not allowed" The value for the motion monitoring time is not allowed.',
    },
    17189: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Target window range not allowed" The value for the target window is not allowed.',
    },
    17190: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Position window range not allowed" The value for the position window is not allowed.',
    },
    17191: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Position window monitoring time not allowed" The value for the position window monitoring time is not allowed.',
    },
    17192: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Loop movement not allowed" The value for the loop movement is not allowed.',
    },
    17193: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Axis cycle time not allowed" The value for the axis cycle time is not allowed.',
    },
    17194: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Stepper motor operating mode not allowed" The value for the stepper motor operating mode is not allowed.',
    },
    17195: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Displacement per stepper motor step not allowed" The value for the displacement associated with one step of the stepper motor is not allowed (step scaling).',
    },
    17196: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Minimum speed for stepper motor set value profile not allowed" The value for the minimum speed of the stepper motor speed profile is not allowed.',
    },
    17197: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Stepper motor stages for one speed stage not allowed" The value for the number of steps for each speed stage in the set value generation is not allowed.',
    },
    17198: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"DWORD for the interpretation of the axis units not allowed" The value that contains the flags for the interpretation of the position and velocity units is not allowed.',
    },
    17199: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Maximum velocity not allowed" The value for the maximum permitted velocity is not allowed.',
    },
    17200: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"Motion monitoring window not allowed" The value for the motion monitoring window is not allowed.',
    },
    17201: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"PEH time monitoring not allowed" The value for the activation of the PEH time monitoring is not allowed (PEH: positioning end and halt).',
    },
    17202: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"PEH monitoring time not allowed" The value for the PEH monitoring time (timeout) is not allowed (PEH: positioning end and halt). default value: 5s',
    },
    17203: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"AXISERR_RANGE_DELAYBREAKRELEASE"',
    },
    17204: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"AXISERR_RANGE_DATAPERSISTENCE"',
    },
    17210: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": '"AXISERR_RANGE_POSDIFF_FADING_ACCELERATION"',
    },
    17211: {
        "Category": "Axis Errors",
        "Error type": "Parameter",
        "Description": "\"Fast Axis Stop Signal Type not allowed\" The value for the Signal Type of the 'Fast Axis Stop' is not allowed [0...5].",
    },
    17216: {
        "Category": "Axis Errors",
        "Error type": "Initialization",
        "Description": '"Axis initialization" Axis has not been initialized. Although the axis has been created, the rest of the initialization has not been performed (1. Initialization of axis I/O, 2. Initialization of axis, 3. Reset axis).',
    },
    17217: {
        "Category": "Axis Errors",
        "Error type": "Address",
        "Description": '"Group address" Axis does not have a group, or the group address has not been initialized (group contains the set value generation).',
    },
    17218: {
        "Category": "Axis Errors",
        "Error type": "Address",
        "Description": '"Encoder address" The axis does not have an encoder, or the encoder address has not been initialized.',
    },
    17219: {
        "Category": "Axis Errors",
        "Error type": "Address",
        "Description": '"Controller address" The axis does not have a controller, or the controller address has not been initialized.',
    },
    17220: {
        "Category": "Axis Errors",
        "Error type": "Address",
        "Description": '"Drive address" The axis does not have a drive, or the drive address has not been initialized.',
    },
    17221: {
        "Category": "Axis Errors",
        "Error type": "Address",
        "Description": '"Axis interface PLC to NC address" Axis does not have an axis interface from the PLC to the NC, or the axis interface address has not been initialized.',
    },
    17222: {
        "Category": "Axis Errors",
        "Error type": "Address",
        "Description": '"Axis interface NC to PLC address" Axis does not have an axis interface from the NC to the PLC, or the axis interface address has not been initialized.',
    },
    17223: {
        "Category": "Axis Errors",
        "Error type": "Address",
        "Description": '"Size of axis interface NC to PLC is not allowed" (INTERNAL ERROR) The size of the axis interface from NC to PLC is not allowed.',
    },
    17224: {
        "Category": "Axis Errors",
        "Error type": "Address",
        "Description": '"Size of axis interface PLC to NC is not allowed" (INTERNAL ERROR) The size of the axis interface from PLC to NC is not allowed.',
    },
    17238: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Controller enable" Controller enable for the axis is not present (see axis interface SPS®NC). This enable is required, for instance, for an axis positioning task.',
    },
    17239: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Feed enable minus" Feed enable for movement in the negative direction is not present (see axis interface SPS®NC).\xa0This enable is required, for instance, for an axis positioning task in the negative direction.',
    },
    17240: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Feed enable plus" Feed enable for movement in the positive direction is not present (see axis interface SPS®NC).\xa0This enable is required, for instance, for an axis positioning task in the positive direction.',
    },
    17241: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Set velocity not allowed" The set velocity requested for a positioning task is not allowed. This can happen if the velocity is less than or equal to zero, larger than the maximum permitted axis velocity, or, in the case of servo-drives, is larger than the reference velocity of the axis (see axis and drive parameters).',
    },
    17242: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Movement smaller than one encoder increment" (INTERNAL ERROR) The movement required of an axis is, in relation to a positioning task, smaller than one encoder increment (see scaling factor). This information is, however, handled internally in such a way that the positioning is considered to have been completed without an error message being returned.',
    },
    17243: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Set acceleration monitoring" (INTERNAL ERROR) The set acceleration has exceeded the maximum permitted acceleration or deceleration parameters of the axis.',
    },
    17244: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"PEH time monitoring" The PEH time monitoring has detected that, after the PEH monitoring time that follows a positioning has elapsed, the target position window has not been reached. The following points must be checked: Is the PEH monitoring time, in the sense of timeout monitoring, set to a sufficiently large value (e.g. 1-5\xa0s)? The PEH monitoring time must be chosen to be significantly larger than the target position monitoring time. Have the criteria for the target position monitoring (range window and time) been set too strictly? Note: The PEH time monitoring only functions when target position monitoring is active!',
    },
    17245: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Encoder existence monitoring / movement monitoring" During the active positioning the actual encoder value has changed continuously for a default check time from NC cycle to NC cycle less than the default minimum movement limit. => Check, whether axis is mechanically blocked, or the encoder system failed, etc... Note: The check is not performed while the axis is logically standing (position control), but only at active positioning (it would make no sense if there is a mechanical holding brake at the standstill)!',
    },
    17246: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Looping distance less than breaking distance" The absolute value of the looping distance is less or equal than the positive or negative breaking distance. This is not allowed.',
    },
    17249: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Time range exceeded (future)" The calculated position lies too far in the future (e.g. when converting a position value in a DC time stamp).',
    },
    17250: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Time range exceeded (past)" The calculated position lies too far in the past (e.g. when converting a position value in a DC time stamp).',
    },
    17251: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Position cannot be determined" The requested position cannot be determined. Case 1: It was not passed through in the past. Case 2: It cannot be reached in future. A reason can be a zero velocity value or an acceleration that causes a turn back.',
    },
    17252: {
        "Category": "Axis Errors",
        "Error type": "Monitoring",
        "Description": '"Position indeterminable (conflicting direction of travel)" The direction of travel expected by the caller of the function deviates from the actual direction of travel (conflict between PLC and NC view, for example when converting a position to a DC time).',
    },
    17312: {
        "Category": "Axis Errors",
        "Error type": "Internal",
        "Description": '"Axis consequential error" Consequential error resulting from another causative error related to another axis. Axis consequential errors can occur in relation to master/slave couplings or with multiple axis interpolating DXD groups.',
    },
    18944: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Table ID not allowed" The value for the table ID is not allowed, e.g. because it has already been assigned, is less than or equal to zero, or is greater than 255.',
    },
    18945: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Table type not allowed" The value for the table type is unacceptable because it is not defined.',
    },
    18946: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Number of lines in the table not allowed" The value of the number of lines in the table is not allowed, because, for example, it is smaller than two at linear interpolation and smaller than four at spline interpolation.',
    },
    18947: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Number of columns in the table is not allowed" The value of the number of columns in the table is not allowed, because, for example, it is less than or equal to zero (depends upon the type of table or slave).',
    },
    18948: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Step size (position delta) not allowed" The value for the step size between two lines (position delta) is not allowed, because, for example, it is less than or equal to zero.',
    },
    18949: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Period not allowed" The value for the period is not allowed, because, for example, it is less than or equal to zero.',
    },
    18950: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Table is not monotonic" The value for the step size is not allowed, because, for example, it is less than or equal to zero.',
    },
    18951: {
        "Category": "Table Errors",
        "Error type": "initialization",
        "Description": "„Table sub type is not allowed“ The value for the table sub type is not allowed or otherwise the table class (slave type) do not match up to the table main type. Table sub type: (1) equidistant linear position table, (2) equidistant cyclic position table, (3) none equidistant linear position table, (4) none equidistant cyclic position table",
    },
    18952: {
        "Category": "Table Errors",
        "Error type": "initialization",
        "Description": "„Table interpolation type is not allowed“ The value for the table interpolation type is allowed. Table interpolation type: (0) linear-interpolation, (1) 4-point-interpolation, (2) spline-interpolation",
    },
    18953: {
        "Category": "Table Errors",
        "Error type": "initialization",
        "Description": "\"Incorrect table main type\" The table main type is unknown or otherwise the table class (slave type) do not match up to the table main type. Table main type: (1) camming table, (2) characteristic table, (3) 'motion function' table (MF)",
    },
    18960: {
        "Category": "Table Errors",
        "Error type": "initialization",
        "Description": '"Table initialization" Table has not been initialized. Although the table has been created, the rest of the initialization has not been performed. For instance, the number of lines or columns may be less than or equal to zero.',
    },
    18961: {
        "Category": "Table Errors",
        "Error type": "initialization",
        "Description": '"Not enough memory" Table could not be created, since there is not enough memory.',
    },
    18962: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": '"Function not executed, function not available" The function has not been implemented, or cannot be executed, for the present type of table.',
    },
    18963: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": '"Line index not allowed" The start line index or the stop line index to be used for read or write access to the table is not allowed. For instance, the line index may be greater than the total number of lines in the table.',
    },
    18964: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": '"Column index not allowed" The start column index or the stop column index to be used for read or write access to the table in not allowed. For instance, the column index may be greater than the total number of columns in the table.',
    },
    18965: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": '"Number of lines not allowed" The number of lines to be read from or written to the table is not allowed. The number of lines must be an integer multiple of the number of elements in a line (n * number of columns).',
    },
    18966: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": '"Number of columns not allowed" The number of columns to be read from or written to the table is not allowed. The number of columns must be an integer multiple of the number of elements in a column (n * number of lines).',
    },
    18967: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": '"Error in scaling or in range entry" The entries in the table header are inconsistent, e.g. the validity range is empty. If the error is generated during the run time it is a run time error and stops the master/slave group.',
    },
    18968: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": '"Multi table slave out of range" The slave master position is outside the table values for the master. The error is a run-time error, and stops the master/slave group.',
    },
    18969: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": '"Solo table underflow" The slave master position is outside the table values for the master. The master value of the equidistant table, to be processed linearly, lies under the first table value. The error is a run-time error, and stops the master/slave group.',
    },
    18970: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": '"Solo table overflow" The slave master position is outside the table values for the master. The master value of the equidistant table, to be processed linearly, lies above the first table value. The error is a run-time error, and stops the master/slave group.',
    },
    18971: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Incorrect execution mode" The cyclic execution mode can only be "true" or "false".',
    },
    18972: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Impermissible parameter" The Fifo parameter is not allowed.',
    },
    18973: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Fifo is empty" The Fifo of the external generator is empty. This can signify end of track or a run time error.',
    },
    18974: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": '"Fifo is full" The Fifo of the external generator is full. It is the user‘s task to continue to attempt to fill the Fifo with the rejected values.',
    },
    18975: {
        "Category": "Table Errors",
        "Error type": "parameter",
        "Description": "„Point-Index of Motion Function invalid“ The point index of a Motion Function Point of a Function Table is invalid. First the point index has to be larger than zero and second it has to be numerical continuously for one column in the Motion Function Table (e.g. 1,2,3,... or 10,11,12,...). Remark: The point index is not online-changeable but must be constant.",
    },
    18976: {
        "Category": "Table Errors",
        "Error type": "initialization",
        "Description": "„No diagonalization of matrix“ The spline can not be calculated. The master positions are not correct.",
    },
    18977: {
        "Category": "Table Errors",
        "Error type": "initialization",
        "Description": "„Number of spline points to less“ The number of points of a cubic spline has to be greater than two.",
    },
    18978: {
        "Category": "Table Errors",
        "Error type": "initialization",
        "Description": "„Fifo must not be overwritten“ Fifo must not be overwritten since then the active line would be overwritten. It is the task of the user to secure that the active line is not modified.",
    },
    18979: {
        "Category": "Table Errors",
        "Error type": "function",
        "Description": "„Insufficient number of Motion Function points“ The number of valid Motion Function points is less than two. Either the entire number of points is to low or the point type of many points is set to Ignore Point.",
    },
    17664: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Controller ID not allowed" The value for the controller ID is not allowed, e.g. because it has already been assigned, is less than or equal to zero, or is greater than 255.',
    },
    17665: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Controller type not allowed" The value for the controller type is unacceptable because it is not defined. Type 1: P-controller (position) . . . Type 7: High/low speed controller Type 8: Stepper motor controller Type 9: Sercos controller',
    },
    17666: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Controller operating mode not allowed" The value for the controller operating mode is not allowed.',
    },
    17667: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Weighting of the velocity pre-control not allowed" The value for the percentage weighting of the velocity pre-control is not allowed. The parameter is pre-set to 1.0 (100%) as standard.',
    },
    17668: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Following error monitoring (position) not allowed" The value for the activation of the following error monitoring is not allowed.',
    },
    17669: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Following error (velocity) not allowed" The value for the activation of the following error monitoring (velocity) is not allowed.',
    },
    17670: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Following error window (position) not allowed" The value for the following error window (maximum allowable following error) is not allowed.',
    },
    17671: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Following error filter time (position) not allowed" The value for the following error filter time (position) is not allowed.',
    },
    17672: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Following error window (velocity) not allowed" The value for the following error window (velocity) is not allowed.',
    },
    17673: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Following error filter time (velocity) not allowed" The value for the following error filter time (velocity) is not allowed.',
    },
    17680: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Proportional gain Kv or Kp (controller) not allowed" position The value for the proportional gain (Kv factor or Kp factor) is not allowed.',
    },
    17681: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Integral-action time Tn (controller) not allowed" position The value for the integral-action time is not allowed (I proportion of the PID T1 controller).',
    },
    17682: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Derivative action time Tv (controller) not allowed" position The value for the derivative action time is not allowed (D proportion of the PID T1 controller).',
    },
    17683: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Damping time Td (controller) not allowed" position The value for the damping time is not allowed (D proportion of the PID T1 controller). Suggested value: 0.1 * Tv',
    },
    17684: {
        "Category": "Controller Errors",
        "Error type": "function",
        "Description": '"Activation of the automatic offset compensation not allowed" Activation of the automatic offset compensation is only possible for certain types of controller (with no I component).',
    },
    17685: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Additional proportional gain Kv or Kp (controller) not allowed" position The value for the second term of the proportional gain (Kv factor or Kp factor) is not allowed.',
    },
    17686: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Reference velocity for additional proportional gain Kv or Kp (controller) not allowed" position The value for the reference velocity percentage data entry, to which the additional proportional gain is applied, is not allowed. The standard setting for the parameter is 0.5 (50%).',
    },
    17687: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Proportional gain Pa (proportion) not allowed" acceleration The value for the proportional gain (Pa factor) is not allowed.',
    },
    17688: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Proportional gain Kv (velocity controller) not allowed" The value for the proportional gain (Kv factor) is not allowed.',
    },
    17689: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": "“Reset time Tn (velocity controller) not allowed” The value for the integral-action time is not allowed (I proportion of the PID T1 controller).",
    },
    17690: {
        "Category": "Controller Errors",
        "Error type": "address",
        "Description": '"CONTROLERR_RANGE_ACCJUMPLIMITINGMODE"',
    },
    17691: {
        "Category": "Controller Errors",
        "Error type": "address",
        "Description": '"CONTROLERR_RANGE_ACCJUMPVALUE"',
    },
    17692: {
        "Category": "Controller Errors",
        "Error type": "address",
        "Description": '"CONTROLERR_RANGE_FILTERTIME"',
    },
    17693: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": "„Dead zone not allowed“ The value for the dead zone from the position error or the velocity error (system deviation) is not allowed (only for complex controller with velocity or torque interface).",
    },
    17696: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": "”Rate time Tv (velocity controller) not allowed” The value for the derivative action time is not allowed (D proportion of the PID T1 controller).",
    },
    17697: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"Damping time Td (velocity controller) not allowed" The value for the damping time is not allowed (D proportion of the PID T1 controller). Suggested value: 0.1 * Tv',
    },
    17698: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"CONTROLERR_RANGE_IOUTPUTLIMIT"',
    },
    17699: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"CONTROLERR_RANGE_DOUTPUTLIMIT"',
    },
    17700: {
        "Category": "Controller Errors",
        "Error type": "parameter",
        "Description": '"CONTROLERR_RANGE_POSIDISABLEWHENMOVING"',
    },
    17728: {
        "Category": "Controller Errors",
        "Error type": "initialization",
        "Description": '"Controller initialization" Controller has not been initialized. Although the controller has been created, the rest of the initialization has not been performed (1. Initialization of controller, 2. Reset controller).',
    },
    17729: {
        "Category": "Controller Errors",
        "Error type": "address",
        "Description": '"Axis address" Controller does not know its axis, or the axis address has not been initialized.',
    },
    17730: {
        "Category": "Controller Errors",
        "Error type": "address",
        "Description": '"Drive address" Controller does not know its drive, or the drive address has not been initialized.',
    },
    17744: {
        "Category": "Controller Errors",
        "Error type": "monitoring",
        "Description": '"Following error monitoring (position)" With active following error monitoring (position) a following error exceedance has occurred, whose magnitude is greater than the following error window, and whose duration is longer than the parameterized following error filter time.',
    },
    17745: {
        "Category": "Controller Errors",
        "Error type": "monitoring",
        "Description": '"Following error monitoring (velocity)" With active following error monitoring (velocity) a velocity following error exceedance has occurred, whose magnitude is greater than the following error window, and whose duration is longer than the parameterized following error filter time.',
    },
    17824: {
        "Category": "Controller Errors",
        "Error type": "monitoring",
        "Description": '"CONTROLERR_RANGE_AREA_ASIDE"',
    },
    17825: {
        "Category": "Controller Errors",
        "Error type": "monitoring",
        "Description": '"CONTROLERR_RANGE_AREA_BSIDE"',
    },
    17826: {
        "Category": "Controller Errors",
        "Error type": "monitoring",
        "Description": '"CONTROLERR_RANGE_QNENN"',
    },
    17827: {
        "Category": "Controller Errors",
        "Error type": "monitoring",
        "Description": '"CONTROLERR_RANGE_PNENN"',
    },
    17828: {
        "Category": "Controller Errors",
        "Error type": "monitoring",
        "Description": '"CONTROLERR_RANGE_AXISIDPRESP0"',
    },
    17408: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Encoder ID not allowed" The value for the encoder ID is not allowed, e.g. because it has already been assigned, is less than or equal to zero, or is bigger than 255.',
    },
    17409: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Encoder type not allowed" The value for the encoder type is unacceptable because it is not defined. Type 1: Simulation (incremental) Type 2: M3000 (24 bit absolute) Type 3: M31x0 (24 bit incremental) Type 4: KL5101 (16 bit incremental) Type 5: KL5001 (24 bit absolute SSI) Type 6: KL5051 (16 bit BISSI)',
    },
    17410: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Encoder mode" The value for the encoder (operating) mode is not allowed. Mode 1: Determination of the actual position Mode 2: Determination of the actual position and the actual velocity (filter)',
    },
    17411: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Encoder counting direction inverted?" The flag for the encoder counting direction is not allowed. Flag 0: Positive encoder counting direction Flag 1: Negative encoder counting direction',
    },
    17412: {
        "Category": "Encoder Errors",
        "Error type": "initialization",
        "Description": '"Referencing status" The flag for the referencing status is not allowed. Flag 0: Axis has not been referenced Flag 1: Axis has been referenced',
    },
    17413: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Encoder increments for each physical encoder rotation" The value for the number of encoder increments for each physical rotation of the encoder is not allowed. This value is used by the software for the calculation of encoder overruns and underruns.',
    },
    17414: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Scaling factor" The value for the scaling factor is not allowed. This scaling factor provides the weighting for the conversion of an encoder increment (INC) to a physical unit such as millimeters or degrees.',
    },
    17415: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Position offset (zero point offset)" The value for the position offset of the encoder is not allowed. This value is added to the calculated encoder position, and is interpreted in the physical units of the encoder.',
    },
    17416: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Modulo factor" The value for the encoder\'s modulo factor is not allowed.',
    },
    17417: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Position filter time" The value for the actual position filter time is not allowed (P-T1 filter).',
    },
    17418: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Velocity filter time" The value for the actual velocity filter time is not allowed (P-T1 filter).',
    },
    17419: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Acceleration filter time" The value for the actual acceleration filter time is not allowed (P-T1 filter).',
    },
    17420: {
        "Category": "Encoder Errors",
        "Error type": "initialization",
        "Description": '"Cycle time not allowed" (INTERNAL ERROR) The value of the SAF cycle time for the calculation of actual values is not allowed (e.g. is less than or equal to zero).',
    },
    17421: {
        "Category": "Encoder Errors",
        "Error type": "initialization",
        "Description": '"" ENCERR_RANGE_UNITFLAGS',
    },
    17422: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Actual position correction / measurement system error correction" The value for the activation of the actual position correction ("measuring system error correction") is not allowed.',
    },
    17423: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Filter time actual position correction" The value for the actual position correction filter time is not allowed (P-T1 filter).',
    },
    17424: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Search direction for referencing cam inverted" The value of the search direction of the referencing cam in a referencing procedure is not allowed. Value 0: Positive direction Value 1: Negative direction',
    },
    17425: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Search direction for sync pulse (zero pulse) inverted" The value of the search direction of the sync pulse (zero pulse) in a referencing procedure is not allowed. Value 0: Positive direction Value 1: Negative direction',
    },
    17426: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Reference position" The value of the reference position in a referencing procedure is not allowed.',
    },
    17427: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Clearance monitoring between activation of the hardware latch and appearance of the sync pulse" (NOT IMPLEMENTED) The flag for the clearance monitoring between activation of the hardware latch and occurrence of the sync/zero pulse ("latch valid") is not allowed. Value 0: Passive Value 1: Active',
    },
    17428: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Minimum clearance between activation of the hardware latch and appearance of the sync pulse" (NOT IMPLEMENTED) The value for the minimum clearance in increments between activation of the hardware latch and occurrence of the sync/zero pulse ("latch valid") during a referencing procedure is not allowed.',
    },
    17429: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"External sync pulse" (NOT IMPLEMENTED) The value of the activation or deactivation of the external sync pulse in a referencing procedure is not allowed. Value 0: Passive Value 1: Active',
    },
    17430: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Scaling of the noise rate is not allowed" The value of the scaling (weighting) of the synthetic noise rate is not allowed. This parameter exists only in the simulation encoder and serves to produce a realistic simulation.',
    },
    17431: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": "„Tolerance window for modulo-start“ The value for the tolerance window for the modulo-axis-start is invalid. The value must be greater or equal than zero and smaller than the half encoder modulo-period (e. g. in the interval [0.0,180.0) ).",
    },
    17432: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": "„Encoder reference mode“ The value for the encoder reference mode is not allowed, resp. is not supported for this encoder type.",
    },
    17433: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": "„Encoder evaluation direction“ The value for the encoder evaluation direction (log. counter direction) is not allowed.",
    },
    17434: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": "„Encoder reference system“ The value for the encoder reference system is invalid (0: incremental, 1: absolute, 2: absolute+modulo).",
    },
    17435: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": "„Encoder position initialization mode“ When starting the TC system the value for the encoder position initialization mode is invalid.",
    },
    17436: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": "„Encoder sign interpretation (UNSIGNED- / SIGNED- data type)“ The value for the encoder sign interpretation (data type) for the encoder the actual increment calculation (0: Default/not defined, 1: UNSIGNED, 2:/ SIGNED) is invalid.",
    },
    17440: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Software end location monitoring minimum not allowed" The value for the activation of the software location monitoring minimum is not allowed.',
    },
    17441: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Software end location monitoring maximum not allowed" The value for the activation of the software location monitoring maximum is not allowed.',
    },
    17442: {
        "Category": "Encoder Errors",
        "Error type": "function",
        "Description": '"Actual value setting is outside the value range" The "set actual value" function cannot be carried out, because the new actual position is outside the expected range of values.',
    },
    17443: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Software end location minimum not allowed" The value for the software end location minimum is not allowed.',
    },
    17444: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '"Software end location maximum not allowed" The value for the software end location maximum is not allowed.',
    },
    17445: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": "„Filter mask for the raw data of the encoder is invalid“ The value for the filter mask of the encoder raw data in increments is invalid.",
    },
    17446: {
        "Category": "Encoder Errors",
        "Error type": "parameter",
        "Description": '„Reference mask for the raw data of the encoder is invalid“ The value for the reference mask (increments per encoder turn, absolute resolution) for the raw data of the encoder is invalid. E.g. this value is used for axis reference sequence (calibration) with the reference mode "Software Sync".',
    },
    17456: {
        "Category": "Encoder Errors",
        "Error type": "function",
        "Description": '"Hardware latch activation (encoder)" Activation of the encoder hardware latch was implicitly initiated by the referencing procedure. If this function has already been activated but a latch value has not yet become valid ("latch valid"), another call to the function is refused with this error.',
    },
    17457: {
        "Category": "Encoder Errors",
        "Error type": "function",
        "Description": '"External hardware latch activation (encoder)" The activation of the external hardware latch (only available on the KL5101) is initiated explicitly by an ADS command (called from the PLC program of the Visual Basic interface). If this function has already been activated, but the latch value has not yet been made valid by an external signal ("external latch valid"), another call to the function is refused with this error.',
    },
    17458: {
        "Category": "Encoder Errors",
        "Error type": "function",
        "Description": '"External hardware latch activation (encoder)" If a referencing procedure has previously been initiated and the hardware still signals a valid latch value ("latch valid"), this function must not be called. In practice, however, this error can almost never occur.',
    },
    17459: {
        "Category": "Encoder Errors",
        "Error type": "function",
        "Description": '"External hardware latch activation (encoder)" If this function has already been initiated and the hardware is still signaling that the external latch value is still valid ("extern latch valid"), a further activation should not be carried out and the commando will be declined with an error (the internal handshake communication between NC and IO device is still active). In that case the validity of the external hardware latch would immediately be signaled, although the old latch value would still be present.',
    },
    17460: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"Encoder function not supported" An encoder function has been activated that is currently not released for use, or which is not even implemented.',
    },
    17461: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": "„Encoder function is already active“ An encoder function can not been activated because this functionality is already active.",
    },
    17472: {
        "Category": "Encoder Errors",
        "Error type": "initialization",
        "Description": '"Encoder initialization" Encoder has not been initialized. Although the axis has been created, the rest of the initialization has not been performed (1. Initialization of axis I/O, 2. Initialization of axis, 3. Reset axis).',
    },
    17473: {
        "Category": "Encoder Errors",
        "Error type": "address",
        "Description": '"Axis address" The encoder does not have an axis, or the axis address has not been initialized.',
    },
    17474: {
        "Category": "Encoder Errors",
        "Error type": "address",
        "Description": '"I/O input structure address" The drive does not have a valid I/O input address in the process image.',
    },
    17475: {
        "Category": "Encoder Errors",
        "Error type": "address",
        "Description": '"I/O output structure address" The encoder does not have a valid I/O output address in the process image.',
    },
    17488: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"Encoder counter underflow monitoring" The encoder\'s incremental counter has underflowed.',
    },
    17489: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"Encoder counter overflow monitoring" The encoder\'s incremental counter has overflowed.',
    },
    17504: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"Software end location minimum (axis start)" With active monitoring of the software end location for a minimum, a start has been made from a position that lies below the software end location minimum.',
    },
    17505: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"Software end location maximum (axis start)" With active monitoring of the software end location for a maximum, a start has been made from a position that lies above the software end location maximum.',
    },
    17506: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"Software end location minimum (positioning process)" With active monitoring of the software end location for a minimum, the actual position has fallen below the software end location minimum. In the case of servo axes (continuously driven axes) this limit is expanded by the magnitude of the parameterized following error window (position).',
    },
    17507: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"Software end location maximum (positioning process)" With active monitoring of the software end location for a maximum, the actual position has exceeded the software end location maximum. In the case of servo axes (continuously driven axes) this limit is expanded by the magnitude of the parameterized following error window (position).',
    },
    17508: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": "„Encoder hardware error“ The drive resp. the encoder system reports a hardware error of the encoder. An optimal error code is displayed in the message of the event log.",
    },
    17509: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": "„Position initialization error at system start“ At the first initialization of the set position was this for all initialization trials (without over-/under-flow, with underflow and overflow ) out of the final position minimum and maximum.",
    },
    17520: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"SSI transformation fault or not finished" The SSI transformation of the FOX 50 module was faulty for some NC-cycles or did not finished respectively.',
    },
    17570: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"ENCERR_ADDR_CONTROLLER"',
    },
    17571: {
        "Category": "Encoder Errors",
        "Error type": "monitoring",
        "Description": '"ENCERR_INVALID_CONTROLLERTYPE"',
    },
    16384: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Internal error" Internal system error in the NC on ring 0, no further details.',
    },
    16385: {
        "Category": "General NC Errors",
        "Error type": "memory",
        "Description": '"Memory error" The ring-0 memory management is not providing the required memory. This is usually a result of another error, as a result of which the controller will halt normal operation (now if not before).',
    },
    16386: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Nc retain data error (persistent data)" Error while loading the Nc retain data. The axes concerned are no longer referenced (status flag "Homed" is set to FALSE). Possible reasons are: - Nc retain data not found - Nc retain data expired (old backup data) - Nc retain data corrupt or inconsistent',
    },
    16400: {
        "Category": "General NC Errors",
        "Error type": "parameter",
        "Description": '"Channel identifier not allowed" Either an unacceptable value (not 1...255) has been used, or a channel that does not exist in the system has been named.',
    },
    16401: {
        "Category": "General NC Errors",
        "Error type": "parameter",
        "Description": '"Group identifier not allowed" Either an unacceptable value (not 1...255) has been used, or a group that does not exist in the system has been named.',
    },
    16402: {
        "Category": "General NC Errors",
        "Error type": "parameter",
        "Description": '"Axis identifier not allowed" Either an unacceptable value (not 1...255) has been used, or an axis that does not exist in the system has been named.',
    },
    16403: {
        "Category": "General NC Errors",
        "Error type": "parameter",
        "Description": '"Encoder identifier not allowed" Either an unacceptable value (not 1...255) has been used, or a encoder that does not exist in the system has been named.',
    },
    16404: {
        "Category": "General NC Errors",
        "Error type": "parameter",
        "Description": '"Controller identifier not allowed" Either an unacceptable value (not 1...255) has been used, or a controller that does not exist in the system has been named.',
    },
    16405: {
        "Category": "General NC Errors",
        "Error type": "parameter",
        "Description": '"Drive identifier not allowed" Either an unacceptable value (not 1...255) has been used, or a drive that does not exist in the system has been named.',
    },
    16406: {
        "Category": "General NC Errors",
        "Error type": "parameter",
        "Description": '"Table identifier not allowed" Either an unacceptable value (not 1...255) has been used, or a table that does not exist in the system has been named.',
    },
    16416: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"No process image" No PLC-axis interface during creation of an axis.',
    },
    16417: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"No process image" No axis-PLC interface during creation of an axis.',
    },
    16418: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"No process image" No encoder-I/O interface during creation of an axis.',
    },
    16419: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"No process image" No I/O-encoder interface during creation of an axis.',
    },
    16420: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"No process image" No drive-I/O interface during creation of an axis.',
    },
    16421: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"No process image" No I/O-drive interface during creation of an axis.',
    },
    16432: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Coupling type not allowed" Unacceptable master/slave coupling type.',
    },
    16433: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Axis type not allowed" Unacceptable type specification during creation of an axis.',
    },
    16448: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Axis is incompatible" Axis is not suitable for the intended purpose. A high speed/low speed axis, for example, cannot function as a slave in an axis coupling.',
    },
    16464: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Channel not ready for operation" The channel is not complete, and is therefore not ready for operation. This is usually a consequence of problems at system start-up.',
    },
    16465: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Group not ready for operation" The group is not complete, and is therefore not ready for operation. This is usually a consequence of problems at system start-up.',
    },
    16466: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Axis not ready for operation" The axis is not complete, and is therefore not ready for operation. This is usually a consequence of problems at system start-up.',
    },
    16480: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Channel exists" The channel that is to be created already exists.',
    },
    16481: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Group exists" The group that is to be created already exists.',
    },
    16482: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Axis exists" The axis that is to be created already exists.',
    },
    16483: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Table exists" The table that is to be created already exists, resp. it is tried internally to use an already existing table id ( e.g. for the universal flying saw).',
    },
    16496: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Axis index not allowed" The location within the channel specified for an axis is not allowed.',
    },
    16497: {
        "Category": "General NC Errors",
        "Error type": "internal",
        "Description": '"Axis index not allowed" The location within the group specified for an axis is not allowed.',
    },
}
