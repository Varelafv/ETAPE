----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 27.09.2022 10:19:38
-- Design Name: 
-- Module Name: clk_div - Behavioral
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
entity clk_div is
    Generic(
    Data :INTEGER :=14
    );
 Port ( 
 mclk : in STD_LOGIC; --CLOCK DU REDPITAYA A 125MG
 rst : in STD_LOGIC:='0';
  Select_n: in INTEGER :=0;
 out_s : out STD_LOGIC:='0'
--out_s : out STD_LOGIC_VECTOR(Data-1 downto 0):=(others =>'0')
 );
 
end clk_div;
architecture Behavioral of clk_div is

Begin
process(mclk,rst)
variable count : std_logic_vector(Data-1 downto 0):=(others =>'0');
begin
if rst='1' then count :=(others =>'0');
    elsif rising_edge(mclk) then
        count := count + 1;
       out_s<= count(Select_n);
        
end if;
end process;

end Behavioral; 
