----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 01.02.2023 14:07:24
-- Design Name:
-- Module Name: CEMES_IP_SPLIT_MIO - Behavioral
-- Project Name:
-- Target Devices:
-- Tool Versions:
-- Description:
--
-- Dependencies:
--
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity CEMES_IP_SPLIT_MIO is
--  Port ( );
    Port (clk : in std_logic;
          DATA_IN : in std_logic_vector (12 downto 0):=(others=>'0');
          Type_Wave_OUT1 : out std_logic_vector (2 downto 0):=(others=>'0');
          Type_Wave_OUT2 : out std_logic_vector (2 downto 0):=(others=>'0');
          GATING_CH1 : out std_logic_vector (2 downto 0):=(others=>'0');
          GATING_CH2 : out std_logic_vector (2 downto 0):=(others=>'0');
          Select_frequence_CH1 : out std_logic_vector(3 downto 0):=(others=>'0');
          Select_frequence_CH2 : out std_logic_vector(3 downto 0):=(others=>'0')
          );


end CEMES_IP_SPLIT_MIO;

architecture Behavioral of CEMES_IP_SPLIT_MIO is
              --    XXXXXXXXXXXX --CREATION DE SIGNAUX -- XXXXXXXXXXXX
signal ADRESS : std_logic_vector (1 downto 0):=(others => '0'); --[0 1 2 3 ]
signal W : std_logic:= '0';
signal R : std_logic:= '0';
signal CHANNEL : std_logic:= '0';
signal DATA : std_logic_vector (7 downto 0):=(others => '0');
begin

  UT:  process(clk)


       begin


               -- XXXXXXXXXXXX--PASSAGE D'INFORMATION -- XXXXXXXXXXXX
              ADRESS <=DATA_IN(1 downto 0 );  ---[ 0 à  3]
              W <=DATA_IN(2);  ---[0 à  1 ]
              R <=DATA_IN(3);  ---[0 à  1 ]
              CHANNEL<=DATA_IN(4);--[0 channel 1  à  1 channel 2]
              DATA <= DATA_IN(12 downto 5);  --[0  à  3 ]
              --
              -- XXXXXXXXXXXX--VERIFIER LE CHANNEL -- XXXXXXXXXXXX

               if CHANNEL= '0' then ---CHANNAL 1
                          -- XXXXXXXXXXXX--  ADRESS 0 TYPE WAVES -- XXXXXXXXXXXX

                       if  ADRESS = "00" then
                          case W is
                            when '1' =>
                               Type_Wave_OUT1 <=  DATA(2 downto 0);
                            when '0' =>
                                Type_Wave_OUT1 <=(others=>'0');
                            when others =>
                              --VIDE
                          end case;
                         -- XXXXXXXXXXXX--  ADRESS 0 TYPE WAVES -- XXXXXXXXXXXX

                -- XXXXXXXXXXXX--  ADRESS 1 GATING-- XXXXXXXXXXXX
                       elsif  ADRESS= "01" then
                          case W is
                             when '1' =>
                               GATING_CH1<=  DATA(2 downto 0);
                             when '0' =>
                             GATING_CH1 <= (others=>'0');
                             when others =>
                               --VIDE
                           end case;

               -- XXXXXXXXXXXX--  ADRESS 2-- XXXXXXXXXXXX
                     elsif  ADRESS="10" then
                            case W is
                              when '1' =>
                               Select_frequence_CH1  <=  DATA(3 downto 0);
                              when '0' =>
                               Select_frequence_CH1 <=( others => '0');
                               when others =>
                               --VIDE
                             end case;
             -- XXXXXXXXXXXX--  ADRESS 3-- XXXXXXXXXXXX
                      end if ;

            elsif CHANNEL='1' then
                      if  ADRESS = "00" then
                          case W is
                            when '1' =>
                               Type_Wave_OUT2 <=  DATA(2 downto 0);
                            when '0' =>
                                Type_Wave_OUT2 <=(others=>'0');
                            when others =>
                              --VIDE
                          end case;
                         -- XXXXXXXXXXXX--  ADRESS 0 TYPE WAVES -- XXXXXXXXXXXX

                -- XXXXXXXXXXXX--  ADRESS 1 GATING-- XXXXXXXXXXXX
                       elsif  ADRESS= "01" then
                          case W is
                             when '1' =>
                               GATING_CH2<=  DATA(2 downto 0);
                             when '0' =>
                             GATING_CH2 <= (others=>'0');
                             when others =>
                               --VIDE
                           end case;

               -- XXXXXXXXXXXX--  ADRESS 2 FREQUENCE -- XXXXXXXXXXXX
                     elsif  ADRESS="10" then
                            case W is
                              when '1' =>
                               Select_frequence_CH2  <=  DATA(3 downto 0);
                              when '0' =>
                               Select_frequence_CH2 <=( others => '0');
                               when others =>
                               --VIDE
                             end case;

                      end if ;


      end if ;
    end process;
end Behavioral;
