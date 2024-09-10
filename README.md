# Rozklady na prvočísla a testy prvočíselnosti

Zápočtový program, 2024

## Co dělá tento kód

V přiloženém souboru `Rozklad.py` se nachází devět funkcí, z nichž

- jedna je testem  prvočíselnosti,
- tři vypočítávají největší společný dělitel,
- dvě nejmenší společný násobek, a
- poslední tři mají za úkol zjistit prvočíselný  rozklad.

Pro funkci `je_prvocislo` zjišťující prvočíselnost daného  čísla je potřebným vstupem intová proměnná větší nebo rovna 2 a výstupem je `bool`. Algoritmus použitý v této funkci je podobný Miller-Rabinovu  testu prvočíselnosti, jak byl popsán v knize Umění programování 2.díl od Donalda Knutha. Přestože je to pravděpodobnostní test, tak v důsledku  25 opakování je pravděpodobnost nesprávného výsledku (asi 1:10^15) nižší než pravděpodobnost, že se uvnitř počítače změní hodnota bitu. Proto je velmi spolehlivý. Jediné číslo, které tento algoritmus nesprávně určí  je 2, kvůli tomuto jedinému případu je tedy v programu daná výjimka.

Další funkcí je `nsd_moderni_euklid`, jejímž vstupem jsou  dvě intové hodnoty a která spočítá největšího společného dělitele  zadaných čísel a výstupem je tedy také intová proměnná. Algoritmus  využitý v tomto případě je, jak již napovídá název, euklidův. Tato  funkce je nejrychlejší z těch, které jsou v tomto souboru.

Další z funkcí počítající největší společný dělitel je  `nsd_rozsireny_euklid`. Vstupem jsou také dvě intové proměnné a výstupem  pouze jedna. Algoritmem je rozšířený euklidův. Ve srovnání s  nsd_moderni_euklid je asi třikrát pomalejší.

Poslední z funkcí počítající největší společný dělitel je  `nsd_dvojkovy`. Vstupem jsou také dvě intové proměnné a výstupem pouze  jedna. Tato funkce využívá Steinův algoritmus. Z těchto tří funkcí je  však nejpomalejší. Je totiž asi šestkrát pomalejší než první z funkcí  (nsd_moderni_euklid).

Další z funkcí je nsn_euklid, která spočítá nejmenší  společný násobek dvou čísel. Stejně jako u předcházejících funkcí jsou  vstupem dvě intové proměnné a výstupem jenom jedna. Algoritmus využívá  funkci nsd_moderni_euklid. Součin zadaných čísel totiž vydělí jejich  největším společným dělitelem.

Druhou funkcí počítající nejmenší společný násobek je  `nsn_rozklad`. Jejím vstupem jsou také dvě intové proměnné a výstupem  pouze jedna. Algoritmus využitý v této funkci je rozložit si obě čísla  na prvočinitele a následně roznásobit největší mocniny jejich  prvočinitelů. V porovnání s nsn_euklid je tato funkce asi padesátkrát  pomalejší.

První z funkcí počítající prvočíselný rozklad je fermat.  Tato funkce z jedné intové proměnné větší nebo rovna 2 vytvoří seřazený  seznam intových proměnných, které jsou její prvočinitelé. Funkce využívá  rekurzivně Fermatův algoritmus, dokud se nedostane na prvočísla.

Druhou z funkcí na prvočíselný rozklad je euler. Tato  funkce z jedné intové proměnné větší nebo rovna 2 vytvoří seřazený  seznam intových proměnných, které jsou její prvočinitelé. I tato používá  rekurzivně Eulerův algoritmus, dokud nerozloží dané číslo na  prvočinitele. Tato funkce je trochu rychlejší než fermat, její nevýhodou je avšak to, že nedokáže rozložit všechny jí předložená čísla. V tomto  případě se objeví ValueError. Ne každé číslo má totiž dva různé rozklady na součet dvou čtverců, které jsou v tomto algoritmu potřebné.

Proto je zde třetí funkce rozklad, která nejprve vyzkouší funkci euler a pokud zkolabuje, tak se spustí pomalejší fermat.

## Návod na instalaci

Kód používá pouze standardní Pythonské knihovny.

## Příklady použití

```python
import Rozklad
print(Rozklad.je_provcislo(129))

```
