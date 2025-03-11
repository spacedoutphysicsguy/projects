ReadMe.txt for data associated with “Antikythera Mechanism Shows Evidence of Disputed Egyptian Lunar Calendar.”

Any data used for publication should cite:
Thoeni, Andrew, Chris Budiselic, and Andrew Ramsey. “Replication Data for: Antikythera Mechanism Shows Evidence of Disputed Egyptian Lunar Calendar.” Harvard Dataverse, 2019. https://doi.org/10.7910/DVN/VJGLVS.

Files Available
1-Fragment_C_Hole_Measurements.csv - Relative x and y coordinates of each hole center measured in mm. From Fiji export. See meta data below.
2-Figure 1-Composite w Hole and Section Numbers.pdf - Figure 1, composite image from this article with section and hole numbers.
3-Figure-2-Engraved_Lines_with_Center.jpg - Figure 2, composite image of Calendar and Zodiac rings' markings with crosshairs locating the identified center of the concentric circles.

Metadata for "Fragment_C_Hole_Measurements.csv"
Section ID - Identifies each porton of Fragment C demarked by fractures on each end. See "Figure 1" and notes below.
Hole - A number assigned to each hole. See "Figure 1."
Inter-hole Distance - The calculated distance to this hole from the previous hole. Holes at the start of a sequence do not have an inter-hole distance. Calculated using the formula sqrt((x1 – x2)2 + (y1 – y2)2).
Mean(x) - the mean X location (mm) as referenced using the scaled coordinate system in ImageJ when hole measurement data were collected. A mean value is present as there were multiple measurements made for each hole in the original data. This dataset is the reduced data used for all analysis reported in the above paper.
Mean(y) - the mean Y location (mm) as referenced using the scaled coordinate system in ImageJ when hole measurement data were collected. A mean value is present as there were multiple measurements made for each hole in the original data. This dataset is the reduced data used for all analysis reported in the above paper.

NOTES
Mean(x) and Mean(y) are the key measures and are the mean x (or y) coordinates of the center of each hole and are presented in mm based on a field present in the images and scaled using the resolution of 20 pixels equalling one millimeter. These settings were input into FIJI scientific image measuring software so the coordinates could be measured in actual scale terms.

Each hole's mean was based on at least three measurements of the hole's center if the measurement was identical, or nearly so, on each measurement event. However, some holes' mean are comprised of up to eight measures. In all cases, to determine measurement saturation, a hole was measured multiple times until we reached a standard deviation lower than the image resolution (0.05 mm).

The Section ID is defined by physical cracks (some even seperations) observable in the image stacks. We identify these sections as they have effects (sometimes significant) on the outcomes of some measures (e.g., measuring a chord across a section break).

As noted above, each hole is assigned a number and the inter-hole distance is the distance from the current hole (n) to the previous hole (n-1). To calculate the distance, a standard two-dimensional formula (see above) was used. This is possible since the images were custom rendered so the surface containing the holes were parallel to the image plane. Since each hole has its own x,y coordinate, a distance between any hole pair can be calculated. This procedure was used to calculate the chord and, solving for simultaneous equations, we made the center's x (or y) coordinate the third, but unknown, variable.

Note that calculating distances across Sections is not recommended as errors are introduced due to physical brakes in the Mechanism.

-- end of ReadMe.txt --