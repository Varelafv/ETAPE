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
          DATA_IN : in std_logic_vector (6 downto 0):=(others=>'0');
          Type_Wave_OUT1 : out std_logic_vector (2 downto 0):=(others=>'0');
          Type_Wave_OUT2 : out std_logic_vector (2 downto 0):=(others=>'0');
          GATING : out std_logic_vector (2 downto 0):=(others=>'0');
          Select_frequence : out std_logic_vector(3 downto 0):=(others=>'0')
          );


end CEMES_IP_SPLIT_MIO;

architecture Behavioral of CEMES_IP_SPLIT_MIO is
              --    XXXXXXXXXXXX --CREATION DE SIGNAUX -- XXXXXXXXXXXX
signal ADRESS : std_logic_vector (1 downto 0):=(others => '0');
signal WR : std_logic:= '0';
signal DATA : std_logic_vector (3 downto 0):=(others => '0');
begin

  UT:  process(clk)

       begin

               -- XXXXXXXXXXXX--PASSAGE D'INFORMATION -- XXXXXXXXXXXX
              ADRESS <=DATA_IN(1 downto 0 );  ---[ 0 à  3]
              WR <=DATA_IN(2);  ---[0 à  1 ]
              DATA <= DATA_IN(6 downto 3);  --[0  à  3 ]
         -- XXXXXXXXXXXX--VARIFICATION DE ADRESS-- XXXXXXXXXXXX

                 -- XXXXXXXXXXXX--  ADRESS 0-- XXXXXXXXXXXX
         if  ADRESS = "00" then
              case WR is
                when '1' =>
                   Type_Wave_OUT1 <=  DATA(2 downto 0);
                when '0' =>
                    Type_Wave_OUT1 <= "000";
                when others =>
                 Type_Wave_OUT1 <= "000";
              end case;
                -- XXXXXXXXXXXX--  ADRESS 1-- XXXXXXXXXXXX
         elsif  ADRESS= "01" then
              case WR is
                 when '1' =>
                   Type_Wave_OUT2 <=  DATA(2 downto 0);
                 when '0' =>
                 Type_Wave_OUT2 <= "000";
                 when others =>
                  Type_Wave_OUT2 <= "000";
               end case;

               -- XXXXXXXXXXXX--  ADRESS 2-- XXXXXXXXXXXX
         elsif  ADRESS="10" then
                case WR is
                  when '1' =>
                   GATING <=  DATA(2 downto 0);
                  when '0' =>
                   GATING <= "000";
                   when others =>
                   GATING <= "000";
                 end case;
             -- XXXXXXXXXXXX--  ADRESS 3-- XXXXXXXXXXXX
         elsif  ADRESS= "11" then
                 case WR is
                  when '1' =>
                  Select_frequence<=  DATA(3 downto 0);
                  when '0' =>
                  Select_frequence<="0000";
                  when others =>
                  Select_frequence<="0000";
                 end case;

         end if ;
    end process;
end Behavioral;
