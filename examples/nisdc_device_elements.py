"""This file contains registers and field info."""
class Register:
    """This class contains all register info."""
    class LPS22HH:
        """This class contains LPS22HH registers info."""
        class ControlRegister:
            """"This class contains different registers info present in LPS22H."""
            INTERRUPT_CFG = "LPS22HH-Control_Register-INTERRUPT_CFG"
            THS_P_L = "LPS22HH-Control_Register-THS_P_L"
            THS_P_H = "LPS22HH-Control_Register-THS_P_H"
            IF_CTRL = "LPS22HH-Control_Register-IF_CTRL"
            WHO_AM_I = "LPS22HH-Control_Register-WHO_AM_I"
            CTRL_REG1 = "LPS22HH-Control_Register-CTRL_REG1"
            CTRL_REG2 = "LPS22HH-Control_Register-CTRL_REG2"
            CTRL_REG3 = "LPS22HH-Control_Register-CTRL_REG3"
            FIFO_CTRL = "LPS22HH-Control_Register-FIFO_CTRL"
            FIFO_WTM = "LPS22HH-Control_Register-FIFO_WTM"
            REF_P_L = "LPS22HH-Control_Register-REF_P_L"
            REF_P_H = "LPS22HH-Control_Register-REF_P_H"
            RESERVED = "LPS22HH-Control_Register-RESERVED"
            RPDS_L = "LPS22HH-Control_Register-RPDS_L"
            RPDS_H = "LPS22HH-Control_Register-RPDS_H"

        class SensorRegister:
            """This class contains sensor registers info."""
            INT_SOURCE = "LPS22HH-Sensor_Register-INT_SOURCE"
            FIFO_STATUS1 = "LPS22HH-Sensor_Register-FIFO_STATUS1"
            FIFO_STATUS2 = "LPS22HH-Sensor_Register-FIFO_STATUS2"
            STATUS = "LPS22HH-Sensor_Register-STATUS"
            PRESS_OUT_XL = "LPS22HH-Sensor_Register-PRESS_OUT_XL"
            PRESS_OUT_L = "LPS22HH-Sensor_Register-PRESS_OUT_L"
            PRESS_OUT_H = "LPS22HH-Sensor_Register-PRESS_OUT_H"
            TEMP_OUT_L = "LPS22HH-Sensor_Register-TEMP_OUT_L"
            TEMP_OUT_H = "LPS22HH-Sensor_Register-TEMP_OUT_H"

        class FifoRegister:
            """This class contains FIFO registers info."""
            FIFO_DATA_OUT_PRESS_XL = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_PRESS_XL"
            FIFO_DATA_OUT_PRESS_L = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_PRESS_L"
            FIFO_DATA_OUT_PRESS_H = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_PRESS_H"
            FIFO_DATA_OUT_TEMP_L = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_TEMP_L"
            FIFO_DATA_OUT_TEMP_H = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_TEMP_H"


class Field:
    """This class contains field info."""
    class LPS22HH:
        """This class contains LPS22HH field info."""
        class ControlRegister:
            """This class contains different field info in LPS22HH register."""
            AUTOREFP = "LPS22HH-Control_Register-AUTOREFP"
            RESET_ARP = "LPS22HH-Control_Register-RESET_ARP"
            AUTOZERO = "LPS22HH-Control_Register-AUTOZERO"
            RESET_AZ = "LPS22HH-Control_Register-RESET_AZ"
            DIFF_EN = "LPS22HH-Control_Register-DIFF_EN"
            LIR = "LPS22HH-Control_Register-LIR"
            PLE = "LPS22HH-Control_Register-PLE"
            PHE = "LPS22HH-Control_Register-PHE"
            THS = "LPS22HH-Control_Register-THS"
            INT_EN_I3C = "LPS22HH-Control_Register-INT_EN_I3C"
            SDA_PU_EN = "LPS22HH-Control_Register-SDA_PU_EN"
            SDO_PU_EN = "LPS22HH-Control_Register-SDO_PU_EN"
            PD_DIS_INT1 = "LPS22HH-Control_Register-PD_DIS_INT1"
            I3C_DISABLE = "LPS22HH-Control_Register-I3C_DISABLE"
            I2C_DISABLE = "LPS22HH-Control_Register-I2C_DISABLE"
            WHO_AM_I_BF = "LPS22HH-Control_Register-WHO_AM_I_BF"
            ODR = "LPS22HH-Control_Register-ODR"
            EN_LPFP = "LPS22HH-Control_Register-EN_LPFP"
            LPFP_CFG = "LPS22HH-Control_Register-LPFP_CFG"
            BDU = "LPS22HH-Control_Register-BDU"
            SIM = "LPS22HH-Control_Register-SIM"
            BOOT = "LPS22HH-Control_Register-BOOT"
            INT_H_L = "LPS22HH-Control_Register-INT_H_L"
            PP_OD = "LPS22HH-Control_Register-PP_OD"
            IF_ADD_INC = "LPS22HH-Control_Register-IF_ADD_INC"
            SWRESET = "LPS22HH-Control_Register-SWRESET"
            LOW_NOISE_EN = "LPS22HH-Control_Register-LOW_NOISE_EN"
            ONE_SHOT = "LPS22HH-Control_Register-ONE_SHOT"
            INT_F_FULL = "LPS22HH-Control_Register-INT_F_FULL"
            INT_F_WTM = "LPS22HH-Control_Register-INT_F_WTM"
            INT_F_OVR = "LPS22HH-Control_Register-INT_F_OVR"
            DRDY = "LPS22HH-Control_Register-DRDY"
            INT_S = "LPS22HH-Control_Register-INT_S"
            STOP_ON_WTM = "LPS22HH-Control_Register-STOP_ON_WTM"
            TRIG_MODES = "LPS22HH-Control_Register-TRIG_MODES"
            F_MODE = "LPS22HH-Control_Register-F_MODE"
            WTM = "LPS22HH-Control_Register-WTM"
            REFL = "LPS22HH-Control_Register-REFL"
            RPDS = "LPS22HH-Control_Register-RPDS"
            RESERVED_1 = "LPS22HH-Control_Register-RESERVED_1"
            RESERVED_2 = "LPS22HH-Control_Register-RESERVED_2"
            RESERVED_3 = "LPS22HH-Control_Register-RESERVED_3"
            RESERVED_4 = "LPS22HH-Control_Register-RESERVED_4"
            RESERVED_5 = "LPS22HH-Control_Register-RESERVED_5"
            RESERVED_6 = "LPS22HH-Control_Register-RESERVED_6"
            RESERVED_7 = "LPS22HH-Control_Register-RESERVED_7"
            RESERVED_8 = "LPS22HH-Control_Register-RESERVED_8"

        class SensorRegister:
            """This class contains sensor register pin info."""
            BOOT_ON = "LPS22HH-Sensor_Register-BOOT_ON"
            IA = "LPS22HH-Sensor_Register-IA"
            PL = "LPS22HH-Sensor_Register-PL"
            PH = "LPS22HH-Sensor_Register-PH"
            RESERVED_9 = "LPS22HH-Sensor_Register-RESERVED_9"
            FSS = "LPS22HH-Sensor_Register-FSS"
            FIFO_WTM_IA = "LPS22HH-Sensor_Register-FIFO_WTM_IA"
            FIFO_OVR_IA = "LPS22HH-Sensor_Register-FIFO_OVR_IA"
            FIFO_FULL_IA = "LPS22HH-Sensor_Register-FIFO_FULL_IA"
            RESERVED_10 = "LPS22HH-Sensor_Register-RESERVED_10"
            T_OR = "LPS22HH-Sensor_Register-T_OR"
            P_OR = "LPS22HH-Sensor_Register-P_OR"
            T_DA = "LPS22HH-Sensor_Register-T_DA"
            P_DA = "LPS22HH-Sensor_Register-P_DA"
            RESERVED_11 = "LPS22HH-Sensor_Register-RESERVED_11"
            POUT = "LPS22HH-Sensor_Register-POUT"
            TOUT = "LPS22HH-Sensor_Register-TOUT"

        class FifoRegister:
            """"This class contains FIFO registers pin info."""
            FIFO_P = "LPS22HH-FIFO_Register-FIFO_P"
            FIFO_T = "LPS22HH-FIFO_Register-FIFO_T"
