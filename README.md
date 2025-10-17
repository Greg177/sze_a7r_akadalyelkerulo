# `sze_a7r_akadalyelkerulo` package
Akadályelkerülő Robot (ROS2, Python)  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Leírás és rövid bemutatás

Ez a kis beadandó egy **autonóm akadályelkerülő rendszer szimulációja** ROS 2-ben, Python nyelven megvalósítva.  
A projekt célja, hogy bemutassa a **publisher-subscriber kommunikációt**, és alapvető **robotvezérlési logikát** vizuális formában, a `turtlesim` csomag segítségével.

---

## Funkcionalitás

- A **Sensor Node** véletlenszerűen generál távolságméréseket (mintha ultrahangos szenzor lenne).
- A **Controller Node** feldolgozza ezeket az értékeket:
  - Ha a távolság nagyobb, mint 1 méter → **"Szabad út" → előre halad**
  - Ha kisebb, mint 1 méter → **"Akadály észlelve" → megáll vagy elfordul**
- A mozgás vizuálisan megjelenik a `turtlesim` ablakban.

---

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/Greg177/sze_a7r_akadalyelkerulo
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select sze_a7r_akadalyelkerulo --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 launch sze_a7r_akadalyelkerulo launch_example1.launch.py
```

## Kommunikációs diagramm

A node-ok és topicok közötti adatáramlás a következő:

```mermaid
graph LR
    A["Szenzor Node"] -->|/distance · std_msgs/Float32| B["Vezérlő Node"]
    B -->|/cmd_vel · geometry_msgs/Twist| C["Robot Mozgatása (Turtlesim)"]

    %% GitHub-kompatibilis stílus
    classDef red fill:#ff9999,stroke:#ff4d4d,color:#000,font-weight:bold;
    classDef blue fill:#99ccff,stroke:#4d94ff,color:#000,font-weight:bold;
    classDef green fill:#99ffb3,stroke:#33cc66,color:#000,font-weight:bold;

    class A red
    class B blue
    class C green