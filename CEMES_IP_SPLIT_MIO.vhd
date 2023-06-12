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
    -- XXXXXXXXXXXX --CREATION DE SIGNAUX -- XXXXXXXXXXXX
    signal ADRESS : std_logic_vector (1 downto 0) := (others => '0'); --[0 1 2 3 ]
    signal W : std_logic := '0';
    signal R : std_logic := '0';
    signal CHANNEL1, CHANNEL2 : std_logic := '0';
    signal DATA : std_logic_vector (7 downto 0) := (others => '0');
	signal signal_Type_Wave_OUT1,signal_Type_Wave_OUT2 : std_logic_vector (2 downto 0) := (others => '0');
begin

    UT: process(clk)
    begin
        -- XXXXXXXXXXXX--PASSAGE D'INFORMATION -- XXXXXXXXXXXX
        ADRESS <= DATA_IN(1 downto 0);  ---MIO54-55
        W <= DATA_IN(2);  ---[0 à  1 ]--MIO56
        R <= DATA_IN(3);  ---[0 à  1 ]--MIO57
        --ATRIBUITION DE BON CHANNAL-----
        if DATA_IN(4) = '0' then
            CHANNEL1 <= not(DATA_IN(4)); --[0 channel 1  à  1 channel 2]--MIO58
            CHANNEL2 <= '0';
        elsif DATA_IN(4) = '1' then
            CHANNEL2 <= DATA_IN(4); --[0 channel 1  à  1 channel 2]--MIO58
            CHANNEL1 <= '0';
        end if;

        DATA <= DATA_IN(12 downto 5); --[0  à  3 ]--MIO59-66

        -- XXXXXXXXXXXX--VERIFIER LE CHANNEL -- XXXXXXXXXXXX
        if CHANNEL1 = '1' then ---CHANNAL 1
            -- XXXXXXXXXXXX--  ADRESS 0 TYPE WAVES -- XXXXXXXXXXXX
            if ADRESS = "00" then
                case W is
                    when '1' =>
                        Type_Wave_OUT1 <= DATA(2 downto 0);
                        signal_Type_Wave_OUT1<= DATA(2 downto 0);
                    when others =>
                        --VIDE
                end case;
            -- XXXXXXXXXXXX--  ADRESS 0 TYPE WAVES -- XXXXXXXXXXXX

            -- XXXXXXXXXXXX--  ADRESS 1 GATING-- XXXXXXXXXXXX
            elsif ADRESS = "01" and signal_Type_Wave_OUT1= "010" then
                case W is
                    when '1' =>
                        GATING_CH1 <= DATA(2 downto 0);
                    when others =>
                        --VIDE
                end case;

            -- XXXXXXXXXXXX--  ADRESS 2-- XXXXXXXXXXXX
            elsif ADRESS = "10" then
                case W is
                    when '1' =>
                        Select_frequence_CH1 <= DATA(3 downto 0);

                    when others =>
                        --VIDE
                end case;
            -- XXXXXXXXXXXX--  ADRESS 3-- XXXXXXXXXXXX
            end if ;

        elsif CHANNEL2 = '1' then
            if ADRESS = "00" then
                case W is
                    when '1' =>
                        Type_Wave_OUT2 <= DATA(2 downto 0);
						signal_Type_Wave_OUT2 <= DATA(2 downto 0);
                    when others =>
                        --VIDE
                end case;
            -- XXXXXXXXXXXX--  ADRESS 0 TYPE WAVES -- XXXXXXXXXXXX

            -- XXXXXXXXXXXX--  ADRESS 1 GATING-- XXXXXXXXXXXX
            elsif ADRESS = "01" and signal_Type_Wave_OUT2= "010" then
                case W is
                    when '1'  =>
                        GATING_CH2 <= DATA(2 downto 0);
                    when others =>
                        --VIDE
                end case;

            -- XXXXXXXXXXXX--  ADRESS 2 FREQUENCE -- XXXXXXXXXXXX
            elsif ADRESS = "10" then
                case W is
                    when '1' =>
                        Select_frequence_CH2 <= DATA(3 downto 0);
                    when others =>
                        --VIDE
                end case;
            end if ;
        end if ;
    end process;
end Behavioral;
