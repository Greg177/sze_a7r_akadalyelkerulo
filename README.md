# `sze_a7r_akadalyelkerulo` package
Akadályelkerülő Robot (ROS2, Python)  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Leírás és rövid bemutatás

Ez a kis beadandó egy **autonóm akadályelkerülő rendszer szimulációja** ROS 2-ben, Python nyelven megvalósítva, ahol a teknős akadályokat érzékelve automatikusan előre halad vagy balra/jobbra fordul, miközben nem hagyja el a szimulációs területet.  


---

## Funkcionalitás

- A **Sensor Node** vagy a **Sim Sensor Node** folyamatosan generál távolságméréseket (mintha ultrahangos szenzor lenne).  
- A **Controller Node** feldolgozza ezeket az értékeket és a teknős pozícióját:  
  - **Szabad út**: nincs akadály a megadott távolságküszöb alatt → a teknős egyenesen halad.  
  - **Akadály észlelve**: a távolság kisebb, mint a küszöb → a teknős egyszer balra vagy jobbra fordul, amíg szabad út nem található.  
  - A falhoz vagy az ablak széléhez érve a teknős automatikusan elfordul, hogy ne hagyja el a szimulációs területet.  
- A mozgás vizuálisan megjelenik a **TurtleSim** ablakban, és a logok jelzik az aktuális állapotot: előrehaladás, fordulás vagy akadály észlelése.

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
ros2 launch sze_a7r_akadalyelkerulo akadalyelkerulo.launch.py
```

## Kommunikációs diagramm

```mermaid
graph LR
    A(["Sensor Node"]) -->|/distance · sensor_msgs/Range| C(["Controller Node"])
    B(["Sim Sensor Node"]) -->|/distance · sensor_msgs/Range| C
    D(["Akadalyelkerulo Node"]) -->|/scan · sensor_msgs/LaserScan| C
    E(["TurtleSim Pose"]) -->|/turtle1/pose · turtlesim/Pose| C
    C -->|/turtle1/cmd_vel · geometry_msgs/Twist| F(["TurtleSim (Robot Mozgatása)"])

    %% --- Stílusok ---
    classDef light fill:#34aec5,stroke:#152742,stroke-width:2px,color:#152742,rx:10,ry:10
    classDef red fill:#ef4638,stroke:#152742,stroke-width:2px,color:#fff,rx:10,ry:10

    class A,B,D,C red
    class F light