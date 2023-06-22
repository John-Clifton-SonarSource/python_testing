void farmDailyRoutine() {
    Crops southEastCrops = getCrops(1, -1);
    Crops eastCrops = getCrops(1, 0);
    WaterContainer waterContainer = new WaterContainer();
    List<Bottle> bottles = new ArrayList<>();
    for(int i = 0; i < 10; i++) {
        var bottle = new Bottle();
        bottle.addWater(10L);
        bottle.putCap();
        bottle.shake(2);
        bottles.add(bottle);
    }
    waterContainer.store(bottles);

    Truck t1 = new Truck(Truck.Type.TRANSPORT);
    t1.load(waterContainer);
    if(Weather.current != Weather.RAINY) {
        WaterContainer extraWaterContainer = new WaterContainer();
        List<Bottle> extraBottles = new ArrayList<>();
        if(southEastCrops.isDry()) {
            for(LandSlot ls : southEastCrops.lands()) {
                Bottle b = new Bottle();
                b.addWater(10L);
                b.putCap();
                extraBottles.add(b);
            }
        } else {
            extraBottles.add(new Bottle());
        }
        if(eastCrops.isDry()) {
            for(LandSlot ls : southEastCrops.lands()) {
                Bottle b = new Bottle();
                b.addWater(10L);
                b.putCap();
                extraBottles.add(b);
            }
        } else {
            extraBottles.add(new Bottle());
        }
        extraWaterContainer.store(extraBottles);
        t1.load(extraWaterContainer);
    } else {
        WaterContainer extraWaterContainer = WaterSource.clone(waterContainer);
        t1.load(extraWaterContainer)
    }
}