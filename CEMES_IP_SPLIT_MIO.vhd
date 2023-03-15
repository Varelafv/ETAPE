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
          GATING : out std_logic_vector (2 downto 0):=(others=>'0');
          Select_frequence : out std_logic_vector(3 downto 0):=(others=>'0')
          );
          
          
end CEMES_IP_SPLIT_MIO;

architecture Behavioral of CEMES_IP_SPLIT_MIO is

begin
    --VALEUR FIXE POUR L'INSTANT 
      
    process(clk)
       begin
        Type_Wave_OUT1 <=DATA_IN(2 downto 0);
        Type_Wave_OUT2 <=DATA_IN(5 downto 3);
        GATING<=DATA_IN(8 downto 6);
        Select_frequence<=DATA_IN(12 downto 9);
       end process; 
end Behavioral;
