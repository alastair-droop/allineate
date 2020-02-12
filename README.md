# Align lines in a file by the first occurrence of a given substring

The `allineate` script aligns each ibnput line so that the first occurrence of a given substring aligns vertically in all input lines.

## Example

The following lines all contain the substring `ctg`:

~~~
CTGTTGAAATGTGTTCACTGAAACATTTTGCTTGCATTAATGCctgtctcttatacacatctccgagcccacgag
GCTCAGGAGTGACAAGTTGCTAATACGCAGAAGGGATGGGTGATACTTCTTGCTTTTCATGATGCATGTTTctgt
TGCTATGACAAGCCTGTCCTCGTCATCATCGCTGCTCACGTCGCTGAAGTGTACctgtctcttatacacatctcc
~~~

After running `allineate` with the search string `ctg` the output is:

~~~
                             CTGTTGAAATGTGTTCACTGAAACATTTTGCTTGCATTAATGC|ctgtctcttatacacatctccgagcccacgag
 GCTCAGGAGTGACAAGTTGCTAATACGCAGAAGGGATGGGTGATACTTCTTGCTTTTCATGATGCATGTTT|ctgt                            
                  TGCTATGACAAGCCTGTCCTCGTCATCATCGCTGCTCACGTCGCTGAAGTGTAC|ctgtctcttatacacatctcc           
~~~

The left and right padding can be shown using `-p:`:

~~~
:::::::::::::::::::::::::::::CTGTTGAAATGTGTTCACTGAAACATTTTGCTTGCATTAATGC|ctgtctcttatacacatctccgagcccacgag
:GCTCAGGAGTGACAAGTTGCTAATACGCAGAAGGGATGGGTGATACTTCTTGCTTTTCATGATGCATGTTT|ctgt::::::::::::::::::::::::::::
::::::::::::::::::TGCTATGACAAGCCTGTCCTCGTCATCATCGCTGCTCACGTCGCTGAAGTGTAC|ctgtctcttatacacatctcc:::::::::::
~~~

## License

This project is licensed under the [The GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) - see the `LICENSE` file for details.

