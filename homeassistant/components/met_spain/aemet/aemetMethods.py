"""class with methods to access AEMET data."""

# https + rest handler
from .aemetClient import aemetClient


class setupAemetHelper(object):
    """Class with helper functions for calling aemet."""

    def __init__(self):
        """Initialize."""

    def verify_fullDateTime(self, parm) -> bool:
        """Verify full data time.

        Format:
            YYYY-MM-DDTHH:MM:SSUTC
        """
        return True

    def verify_regionCode(self, parm) -> bool:
        """Verify region.

        Format:
            esp -> España
            61  -> Andalucía
            62  -> Aragón
            63  -> Asturias, Principado de
            64  -> Ballears, Illes
            78  -> Ceuta
            65  -> Canarias
            66  -> Cantabria
            67  -> Castilla y León
            68  -> Castilla - La Mancha
            69  -> Cataluña
            77  -> Comunitat Valenciana
            70  -> Extremadura
            71  -> Galicia
            72  -> Madrid, Comunidad de
            79  -> Melilla
            73  -> Murcia, Región de
            74  -> Navarra, Comunidad Foral de
            75  -> País Vasco
            76  -> Rioja, La
        """
        return True

    def verify_forestRegion(self, parm) -> bool:
        """Verify forest region.

        Format:
            p -> Península
            b -> Baleares
            c -> Canarias
        """
        return True

    def verify_3day(self, parm) -> bool:
        """Verify 3 day future.

        Format:
            1 -> d + 1
            2 -> d + 2
            3 -> d + 3
        """
        return True


class aemetMethods(object):
    """Class with methods to access AEMET data."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient()

    # --- Meteorological phenomena warnings. ---

    async def warningsMeteorologicalPhenomenaArchive(self, startDT, endDT):
        """Meteorological phenomena warnings, archive.

        Advisories of adverse Meteorological Phenomena either newest or
        for the selected date range.

        :param str(verify_fullDateTime) startDT,
        :param str(verify_fullDateTime) endDT
        """
        url = "avisos_cap/archivo/fechaini/" + startDT + "/fechafin/" + endDT
        return self._aemetClient.request(url)

    async def warningsMeteorologicalPhenomena(self, area):
        """Meteorological phenomena warnings, newest.

        Advisories of adverse Meteorological Phenomena either newest or
        for the selected area.

        :param str(verify_regionCode) area
        """
        url = "avisos_cap/ultimoelaborado/area/" + area
        return self._aemetClient.request(url)

    # --- Fire rates. ---

    async def forestFireRiskMap(self, area):
        """Meteorological risk map with estimated levels of forest fires.

        Last map prepared with estimated meteorological risk levels for
        forest fires in the selected area

        :param str(verify_forestRegion) area
        """
        url = "incendios/mapasriesgo/estimado/area/" + area
        return self._aemetClient.request(url)

    async def forestFireRiskMapFuture(self, day, area):
        """Meteorological risk map with estimated levels of forest fires.

        Last map prepared with estimated meteorological risk levels for
        forest fires in the selected area

        :param str(verify_3day) day
        :param str(verify_forestRegion) area
        """
        url = "incendios/mapasriesgo/previsto/dia/" + day + "/area/" + area
        return self._aemetClient.request(url)

    # --- Satellite information ---

    async def satelliteVegetationImage(self):
        """Image of normalized vegetation index.

        This image is made with a combination of the channel data visible
        and near infrared from the NOAA-19 satellite, which gives us an
        idea of the development of the vegetation. This is so because the
        vegetation strongly absorbs visible channel radiation but strongly
        reflects the near infrared one. This image is renewed on Thursdays
        at the last minute and contains the accumulated data from the last
        week.
        """
        url = "/api/satelites/producto/nvdi"
        return self._aemetClient.request(url)

    async def satelliteSeaWaterTemperatura(self):
        """Image of sea water temperature.

        Image obtained with a combination of channel data infrared from
        the NOAA-19 satellite, which gives us the temperature from the sea
        surface. This image is renewed every day at the last minute and
        contains the accumulated data of the last seven days.
        """
        url = "satelites/producto/sst"
        return self._aemetClient.request(url)


    # --- Specific information of the municipalities in Spain ---

    async def municipalityInformation(self, municipality):
        """Municipality information.

        get information about the selected municipality

        :param str municipality: see getMunicipalities()
        """
        url = "maestro/municipio/" + municipality
        return self._aemetClient.request(url)

    async def getMunicipalities(self):
        """Get list of municipalities

        Returns all the municipalities in Spain.
        This service is useful for obtaining information to use other
        elements of AEMET OpenData, such as the prediction of
        municipalities for 7 days or by hours since it returns the id
        of the municipality that we need.
        """
        url = "maestro/municipios"
        return self._aemetClient.request(url)


    # --- Maps and grafics ---

    async def mapNewestAnalysis(self):
        """Analysis maps. Newest.

        These maps show the configuration of the surface pressure using
        isobars (lines of equal pressure), high areas (A, a) and low (B, b)
        pressure and fronts in Europe and the North Atlantic.
        The analysis map presents the state of the atmosphere at the time
        corresponding and the most relevant phenomena observed in Spain.
        Update frequency: every 12 hours (00, 12).
        """
        url = "mapasygraficos/analisis"
        return self._aemetClient.request(url)

    async def mapSignificantArchive(self, fecha, ambito, dia):
        """Significant maps. Real time.

        Mapas significativos de ámbito nacional o CCAA,
        para una fecha dada y ese mismo día (D+0), al día siguiente (D+1)
        o a los dos días (D+2), en el periodo horario de (00_12) ó (12-24).

        :param str fecha: Fecha de elaboración (AAAA-MM-DD)
        :param str ambito: Ámbito
                                esp -> España
                                and -> Andalucía
                                arn -> Aragón
                                ast -> Asturias
                                bal -> Ballears, Illes
                                coo -> Canarias
                                can -> Cantabria
                                cle -> Castilla y León
                                clm -> Castilla - La Mancha
                                cat -> Cataluña
                                val -> Comunitat Valenciana
                                ext -> Extremadura
                                gal -> Galicia
                                mad -> Madrid, Comunidad de
                                mur -> Murcia, Región de
                                nav -> Navarra, Comunidad Foral de
                                pva -> País Vasco
                                rio -> Rioja, La
        :param str dia: Código de día
                            a -> D+0 (00-12)
                            b -> D+0 (12-24)
                            c -> D+1 (00-12)
                            d -> D+1 (12-24)
                            e -> D+2 (00-12)
                            f -> D+2 (12-24)
        """
        return self._aemetClient.request(
            "/api/mapasygraficos/mapassignificativos/fecha/" + fecha + "/ambito/" + dia
        )

    async def mapSignificantFuture(self, ambito, dia):
        """Mapas significativos. Tiempo actual.

        Mapas significativos de ámbito nacional o CCAA,
        para el día actual (D+0), al día siguiente (D+1)
        o a los dos días (D+2), en el periodo horario de (00_12) ó (12-24).

        :param str ambito: Ámbito
                                esp -> España
                                and -> Andalucía
                                arn -> Aragón
                                ast -> Asturias
                                bal -> Ballears, Illes
                                coo -> Canarias
                                can -> Cantabria
                                cle -> Castilla y León
                                clm -> Castilla - La Mancha
                                cat -> Cataluña
                                val -> Comunitat Valenciana
                                ext -> Extremadura
                                gal -> Galicia
                                mad -> Madrid, Comunidad de
                                mur -> Murcia, Región de
                                nav -> Navarra, Comunidad Foral de
                                pva -> País Vasco
                                rio -> Rioja, La
        :param str dia: Código de día
                            a -> D+0 (00-12)
                            b -> D+0 (00-12)
                            c -> D+1 (00-12)
                            d -> D+1 (12-24)
                            e -> D+2 (00-12)
                            f -> D+2 (12-24)
        """
        return self.aemetClient.request(
            "/api/mapasygraficos/mapassignificativos/" + ambito + "/" + dia
        )


class ObservacionConvencionalApi(object):
    """Datos de observación."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient

    async def datos_de_observacin__tiempo_actual_(self):
        """Datos de observación. Tiempo actual.

        Datos de observación horarios de las últimas 24 horas
        todas las estaciones meteorológicas de las que se han recibido
        datos en ese período. Frecuencia de actualización: continuamente.
        """
        return self._aemetClient.request("/api/observacion/convencional/todas")

    async def datos_de_observacin__tiempo_actual_1(self, idema):
        """Datos de observación. Tiempo actual.

        Datos de observación horarios de las últimas 24 horas
        de la estación meterológica que se pasa como parámetro (idema).
        Frecuencia de actualización: continuamente.

        :param str idema: Índicativo climatológico de la EMA
        """
        return self._aemetClient.request(
            "/api/observacion/convencional/datos/estacion/" + idema
        )

    async def mensajes_de_observacin__ltimo_elaborado_(self, tipomensaje):
        """Mensajes de observación. Último elaborado.

        Últimos mensajes de observación. Para los SYNOP y TEMP devuelve
        los mensajes de las últimas 24 horas y para los CLIMAT de
        los 40 últimos dias. Se pasa como parámetro el tipo de mensaje
        que se desea (tipomensaje). El resultado de la petición es
        un fichero en formato tar.gz, que contiene los boletines en
        formato json y bufr.

        :param str tipomensaje: Tipo de Mensaje
                                    climat -> CLIMAT
                                    synop  -> SYNOP
                                    temp   -> TEMP
        """
        return self._aemetClient.request(
            "/api/observacion/convencional/mensajes/tipomensaje/" + tipomensaje
        )


class PrediccionMaritimaApi(object):
    """Predicción marítima."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient

    async def prediccin_martima_costera_(self, costa):
        """Predicción marítima costera.

        Predicción para un periodo de 24 horas de las condiciones
        meteorológicas para la zona costera pasada por parámetro.

        :param str costa: Área Costera
                            42 -> Costa de Andalucía Occidental y Ceuta
                            47 -> Costa de Andalucía Oriental y Melilla
                            41 -> Costa de Asturias, Cantabria y País Vasco
                            45 -> Costa de Cataluña
                            40 -> Costa de Galicia
                            44 -> Costa de Illes Balears
                            43 -> Costa de las Islas Canarias
                            46 -> Costa de Valencia y Murcia
        """
        return self._aemetClient.request(
            "/api/prediccion/maritima/costera/costa/" + costa
        )

    async def prediccin_martima_de_alta_mar_(self, area):
        """Predicción marítima de alta mar.

        Predicción para un periodo de 24 horas de las condiciones
        meteorológicas para el área marítima pasada por parámetro.

        :param str area:  Área de Alta Mar
                                0 -> Océano Atlántico al sur de 35º N
                                1 -> Océano Atlántico al norte de 30º N
                                2 -> Mar Mediterráneo
        """
        return self._aemetClient.request(
            "/api/prediccion/maritima/altamar/area/" + area
        )


class PrediccionesEspecificasApi(object):
    """Información nivológica para la zona montañosa."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient

    async def informacion_nivologica_(self, area):
        """Información nivológica.

        Información nivológica para la zona montañosa que se pasa
        como parámetro (area).

        :param str area:  Código de Área Montañosa
                                0 -> Pirineo Catalán
                                1 -> Pirineo Navarro y Aragonés
        """
        return self._aemetClient.request(
            "/api/prediccion/especifica/nivologica/" + area
        )

    async def prediccin_de_montaa__tiempo_actual_(self, area, dia):
        """Predicción de montaña. Tiempo actual.

        Predicción meteorológica para la zona montañosa que se pasa
        como parámetro (area) con validez para el día (día).
        Periodicidad de actualización: continuamente.

        :param str area: Código de Área Montañosa
                            peu1 -> Picos de Europa
                            nav1 -> Pirineo Navarro
                            arn1 -> Pirineo Aragonés
                            cat1 -> Pirineo Catalán
                            rio1 -> Ibérica Riojana
                            arn2 -> Ibérica Aragonesa
                            mad2 -> Sierras de Guadarrama y Somosierra
                            gre1 -> Sierra de Gredos
                            nev1 -> Sierra Nevada
        :param str dia: Código de día
                            0 -> día actual
                            1 -> d+1 (mañana)
                            2 -> d+2 (pasado mañana)
                            3 -> d+3 (siguente a pasado mañana)
        """
        return self._aemetClient.request(
            "/api/prediccion/especifica/montaña/pasada/area/" + area + "/dia/" + dia
        )

    async def prediccin_de_montaa__tiempo_pasado_(self, area):
        """Predicción de montaña. Tiempo pasado.

        Breve resumen con lo más significativo de las condiciones
        meteorológicas registradas en la zona de montaña que se pasa como
        parámetro (area) en las últimas 24-36 horas.

        :param str area: Código de Área Montañosa
                            peu1 -> Picos de Europa
                            nav1 -> Pirineo Navarro
                            arn1 -> Pirineo Aragonés
                            cat1 -> Pirineo Catalán
                            rio1 -> Ibérica Riojana
                            arn2 -> Ibérica Aragonesa
                            mad2 -> Sierras de Guadarrama y Somosierra
                            gre1 -> Sierra de Gredos
                            nev1 -> Sierra Nevada
        """
        return self._aemetClient.request(
            "/api/prediccion/especifica/montaña/pasada/area/" + area
        )

    async def prediccin_de_radiacin_ultravioleta__uvi_(self, dia):
        """Predicción de radiación ultravioleta (UVI).

        Predicción de Índice de radiación UV máximo en condiciones
        de cielo despejado para el día seleccionado.

        :param str dia: Código de día
                            0 -> día actual
                            1 -> d+1 (mañana)
                            2 -> d+2 (pasado mañana)
                            3 -> d+3 (dentro de 3 días)
                            4 -> d+4 (dentro de 4 días)
        """
        return self._aemetClient.request("/api/prediccion/especifica/uvi/" + dia)

    async def prediccin_para_las_playas__tiempo_actual_(self, playa):
        """Predicción para las playas. Tiempo actual.

        La predicción diaria de la playa que se pasa como parámetro.
        Establece el estado de nubosidad para unas horas determinadas,
        las 11 y las 17 hora oficial. Se analiza también si se espera
        precipitación en el entorno de esas horas,
        entre las 08 y las 14 horas y entre las 14 y 20 horas.

        :param str playa: Código de playa
                                http://www.aemet.es/documentos/es/eltiempo/prediccion/playas/Playas_codigos.csv
        """
        return self._aemetClient.request("/api/prediccion/especifica/playa/" + playa)

    async def prediccin_por_municipios_diaria__tiempo_actual_(self, municipio):
        """Predicción por municipios diaria. Tiempo actual.

        Predicción para el municipio que se pasa como parámetro (municipio).
        Periodicidad de actualización: continuamente.

        :param str municipio: Código de municipio
                                    http://www.ine.es/daco/daco42/codmun/codmunmapa.htm
        """
        return self._aemetClient.request(
            "/api/prediccion/especifica/municipio/diaria/" + municipio
        )

    async def prediccin_por_municipios_horaria__tiempo_actual_(self, municipio):
        """Predicción por municipios horaria. Tiempo actual.

        Predicción horaria para el municipio que se pasa como parámetro
        (municipio). Presenta la información de hora en hora hasta 48 horas.

        :param str municipio: Código de municipio
                                    http://www.ine.es/daco/daco42/codmun/codmunmapa.htm
        """
        return self._aemetClient.request(
            "/api/prediccion/especifica/municipio/horaria/" + municipio
        )


class PrediccionesNormalizadasTextoApi(object):
    """Predicción normalizadas."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient

    async def prediccin_ccaa_hoy__archivo_(self, ccaa, fecha):
        """Predicción CCAA hoy. Archivo.

        Predicción para la comunidad autónoma que se pasa como parámetro
        (ccaa) con validez para el día de fecha de elaboración que se
        pasa como parámetro (fecha).
        Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
                                and -> Andalucía
                                arn -> Aragón
                                ast -> Astrrias
                                bal -> Ballears, Illes
                                coo -> Canarias
                                can -> Cantabria
                                cle -> Castilla y León
                                clm -> Castilla - La Mancha
                                cat -> Cataluña
                                val -> Comunitat Valenciana
                                ext -> Extremadura
                                gal -> Galicia
                                mad -> Madrid, Comunidad de
                                mur -> Murcia, Región de
                                nav -> Navarra, Comunidad Foral de
                                pva -> País Vasco
                                rio -> Rioja, La
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/ccaa/hoy/" + ccaa + "/elaboracion/" + fecha
        )

    async def prediccin_ccaa_hoy__tiempo_actual_(self, ccaa):
        """Predicción CCAA hoy. Tiempo actual.

        Predicción para la CCAA que se pasa como parámetro con validez
        para mismo día que la fecha de petición. En el caso de que en la
        fecha de petición este producto todavía no se hubiera elaborado,
        se retornará el último elaborado. Actualización continuamente.

        :param str ccaa: Código de CCAA
        """
        return self._aemetClient.request("/api/prediccion/ccaa/hoy/" + ccaa)

    async def prediccin_ccaa_maana__archivo_(self, ccaa, fecha):
        """Predicción CCAA mañana. Archivo.

        Predicción para la comunidad autónoma que se pasa como parámetro
        (ccaa) con validez para el día siguiente a la fecha de elaboración
        que se pasa como parámetro (fecha).
        Periodicidad de actualización. continuamente.

        :param str ccaa: Código de CCAA
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/ccaa/manana/" + ccaa + "/elaboracion/" + fecha
        )

    async def prediccin_ccaa_maana__tiempo_actual_(self, ccaa):
        """Predicción CCAA mañana. Tiempo actual.

        Predicción para la comunidad autónoma que se pasa como parámetro
        para el día siguiente a la fecha de la petición.
        En el caso de el producto no se hubiera elaborado todavía en
        la fecha de petición se retornará el último producto elaborado.
        Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
        """
        return self._aemetClient.request("/api/prediccion/ccaa/manana/" + ccaa)

    async def prediccin_ccaa_medio_plazo__archivo_(self, ccaa, fecha):
        """Predicción CCAA medio plazo. Archivo.

        Predicción de mediio plazo para la comunidad autónoma que se pasa
        como parámetro (ccaa) a partir de la fecha de elaboración que se
        pasa como parámetro (fecha).
        Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/ccaa/medioplazo/" + ccaa + "/elaboracion/" + fecha
        )

    async def prediccin_ccaa_medio_plazo__tiempo_actual_(self, ccaa):
        """Predicción CCAA medio plazo. Tiempo actual.

        Predicción para la comunidad autónoma que se pasa como parámetro
        (ccaa) y con validez para el medio plazo a partir de la fecha de
        petición. En el caso de que en el fecha de la petición no se
        hubiera generado aún el producto, se retornará el última elaborado.
        Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
        """
        return self._aemetClient.request("/api/prediccion/ccaa/medioplazo/" + ccaa)

    async def prediccin_ccaa_pasado_maana__archivo_(self, ccaa, fecha):
        """Predicción CCAA pasado mañana. Archivo.

        Predicción para la comunidad autónoma que se pasa como parámetro
        (ccaa) y validez para pasado mañana a partir de la fecha de
        elaboración que se pasa como parámetro (fecha).
        Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/ccaa/pasadomanana/" + ccaa + "/elaboracion/" + fecha
        )

    async def prediccin_ccaa_pasado_maana__tiempo_actual_(self, ccaa):
        """Predicción CCAA pasado mañana. Tiempo actual.

        Predicción para la comunidad autónoma que se pasa como parámetro
        (ccaa) y validez para el medio plazo a partir de la fecha de
        la petición. En el caso de que en la fecha de la petición dicho
        producto aún no se hubiera generado retornará el último de este
        tipo que se hubiera generado.
        Periodicidad de actualización: continuamente.

        :param str ccaa:  | Código de CCAA
        """
        return self._aemetClient.request("/api/prediccion/ccaa/pasadomanana/" + ccaa)

    async def prediccin_nacional_hoy__archivo_(self, fecha):
        """Predicción nacional hoy. Archivo.

        Predicción nacional para el día correspondiente a la fecha que se
        pasa como parámetro en en formato texto. Actualización diaria.
        Hay días en los que este producto no se realiza.
        En ese caso se devuelve un 404 producto no existente.

        :param str fecha: Fecha en formato (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/nacional/hoy/elaboracion/" + fecha
        )

    async def prediccin_nacional_hoy__tiempo_actual_(self):
        """Predicción nacional hoy. Última elaborada.

        Predicción nacional para el día actual a la fecha de elaboración
        en formato texto. Actualización diaria. Hay días en los que este
        producto no se realiza. En ese caso se devuelve la predicción
        nacional última que se elaboró.
        """
        return self._aemetClient.request("/api/prediccion/nacional/hoy")

    async def prediccin_nacional_maana__archivo_(self, fecha):
        """Predicción nacional mañana. Archivo.

        Predicción nacional para el día siguiente a la fecha de
        elaboración. En este caso la fecha de elaboración es la fecha que
        se pasa como parámetro. Actualización diaria.

        :param str fecha: Día (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/nacional/manana/elaboracion/" + fecha
        )

    async def prediccin_nacional_maana__tiempo_actual_(self):
        """Predicción nacional mañana. Tiempo actual.

        Predicción nacional para el día siguiente a la fecha de
        elaboración. En este caso la fecha de elaboración es el día actual.
        Actualización diaria. En el caso de que en el día actual
        todavía no se haya elaborado se devolverá el último producto de
        predicción nacional para mañana elaborado.
        """
        return self._aemetClient.request("/api/prediccion/nacional/manana")

    async def prediccin_nacional_medio_plazo__archivo_(self, fecha):
        """Predicción nacional medio plazo. Archivo.

        Predicción nacional para el medio plazo siguiente a la fecha de
        elaboración. En este caso, la fecha de elaboración es la fecha que
        se pasa como parámetro. Actualización diaria.

        :param str fecha: Día (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/nacional/medioplazo/elaboracion/" + fecha
        )

    async def prediccin_nacional_medio_plazo__tiempo_actual_(self):
        """Predicción nacional medio plazo. Tiempo actual.

        Predicción nacional para medio plazo siguiente a la fecha de
        elaboración. En este caso la fecha de elaboración es el día actual.
        Actualización diaria. En el caso de que en el día actual
        todavía no se haya elaborado se devolverá el último producto de
        predicción nacional para medio plazo elaborado.
        """
        return self._aemetClient.request("/api/prediccion/nacional/medioplazo")

    async def prediccin_nacional_pasado_maana__archivo_(self, fecha):
        """Predicción nacional pasado mañana. Archivo.

        Predicción nacional para pasado mañana siguiente a la fecha
        de elaboración. En este caso, la fecha de elaboración es la fecha
        que se pasa como parámetro. Actualización diaria.

        :param str fecha: Día (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/nacional/pasadomanana/elaboracion/" + fecha
        )

    async def prediccin_nacional_pasado_maana__tiempo_actual_(self):
        """Predicción nacional pasado mañana. Tiempo actual.

        Predicción nacional para pasado mañana siguiente a la fecha de
        elaboración. En este caso la fecha de elaboración es el día actual.
        Actualización diaria. En el caso de que en el día actual todavía
        no se haya elaborado se devolverá el último producto de
        predicción nacional para pasado mañana elaborado.
        """
        return self._aemetClient.request("/api/prediccion/nacional/pasadomanana")

    async def prediccin_nacional_tendencia__archivo_(self, fecha):
        """Predicción nacional tendencia. Archivo.

        Predicción nacional para tendencia siguiente a la fecha de
        elaboración.
        En este caso, la fecha de elaboración es la fecha que se pasa
        como parámetro. Actualización diaria.

        :param str fecha: Día (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/nacional/tendencia/elaboracion/" + fecha
        )

    async def prediccin_nacional_tendencia__tiempo_actual_(self):
        """Predicción nacional tendencia. Tiempo actual.

        Predicción nacional para tendencia siguiente a la fecha de
        elaboración.
        En este caso la fecha de elaboración es el día actual.
        Actualización diaria.
        En el caso de que en el día actual todavía no se haya elaborado
        se devolverá el último producto de predicción nacional para
        tendencia elaborado.
        """
        return self._aemetClient.request("/api/prediccion/nacional/tendencia")

    async def prediccin_provincia_hoy__archivo_(self, provincia, fecha):
        """Predicción provincia hoy. Archivo.

        Predicción del día siguiente a la fecha que se pasa como parámetro
        para la provincia que se pasa como parámetro.
        Actualización continua y fija a las 14:00 Hora Oficial Peninsular
        del día que se pasa como parámetro.

        :param str provincia: Código Provincia
                                    01 -> Araba/Álaba
                                    01 -> Araba/Álava
                                    02 -> Albacete
                                    03 -> Alacant/Alicante
                                    04 -> Almería
                                    33 -> Asturias
                                    05 -> Ávila
                                    06 -> Badajoz
                                    07 -> Illes Ballears
                                    08 -> Barcelona
                                    48 -> Bizkaia
                                    09 -> Burgos
                                    10 -> Cáceres
                                    11 -> Cádiz
                                    39 -> Cantabria
                                    12 -> Castelló/Castellón
                                    51 -> Ceuta
                                    13 -> Ciudad Real
                                    14 -> Córdoba
                                    15 -> A Coruña
                                    16 -> Cuenca
                                    17 -> Girona
                                    18 -> Granada
                                    19 -> Guadalajara
                                    20 -> Gipuzkoa
                                    21 -> Huelva
                                    22 -> Huesca
                                    23 -> Jaén
                                    24 -> León
                                    25 -> Lleida
                                    27 -> Lugo
                                    28 -> Madrid
                                    29 -> Málaga
                                    52 -> Melilla
                                    30 -> Murcia
                                    31 -> Navarra
                                    32 -> Oursense
                                    34 -> Palencia
                                    35 -> Las Palmas
                                    36 -> Pontevedra
                                    26 -> La Rioja
                                    37 -> Salamanca
                                    38 -> Santa Cruz de Tenerife
                                    40 -> Segovia
                                    41 -> Sevilla
                                    42 -> Soria
                                    43 -> Tarragona
                                    44 -> Teruel
                                    45 -> Toledo
                                    46 -> València/Valencia
                                    47 -> Valladolid
                                    49 -> Zamora
                                    50 -> Zaragoza
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/provincia/hoy/" + provincia + "/elaboracion/" + fecha
        )

    async def prediccin_provincia_hoy__tiempo_actual_(self, provincia):
        """Predicción provincia hoy. Tiempo actual.

        Predicción del día actual para la provincia que se pasa como
        parámetro.
        En el caso de que este producto no se haya elaborado todavía en
        el día actual, se retorna el último elaborado.
        Actualización continua y fija a las 14:00 Hora Oficial Peninsular.

        :param str provincia: Código Provincia
        """
        return self._aemetClient.request("/api/prediccion/provincia/hoy/" + provincia)

    async def prediccin_provincia_maana__archivo_(self, provincia, fecha):
        """Predicción provincia mañana. Archivo.

        Predicción del día siguiente a la fecha que se pasa como parámetro
        para la provincia que se pasa como parámetro.
        Actualización continua y fija a las 14:00 Hora Oficial Peninsular
        del día que se pasa como parámetro.

        :param str provincia: Código Provincia
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        return self._aemetClient.request(
            "/api/prediccion/provincia/manana/" + provincia + "/elaboracion/" + fecha
        )

    async def prediccin_provincia_maana__tiempo_actual_(self, provincia):
        """Predicción provincia mañana. Tiempo actual.

        Predicción del día siguiente para la provincia que se pasa como
        parámetro.
        En el caso de que este producto no se haya elaborado todavía en
        el día actual, se retorna el último elaborado.
        Actualización continua y fija a las 14:00 Hora Oficial Peninsular.

        :param str provincia: Código Provincia
        """
        return self._aemetClient.request(
            "/api/prediccion/provincia/manana/" + provincia
        )


class ProductosClimatologicosApi(object):
    """Balance nacional."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient

    async def balance_hdrico_nacional__documento_(self, anio, decena):
        """Balance hídrico nacional (documento).

        Se obtiene, para la decema y el año pasados por parámetro,
        el Boletín Hídrico Nacional que se elabora cada diez días.
        Se presenta información resumida de forma distribuida para todo
        el territorio nacional de diferentes variables, en las que se
        incluye informaciones de la precipitación y la evapotranspiración
        potencial acumuladas desde el 1 de septiembre.

        :param str anio: Año (AAAA)
        :param str decena: Decena de 01 (primera decena) a 36 (última decena)
        """
        return self._aemetClient.request(
            "/api/productos/climatologicos/balancehidrico/" + anio + "/" + decena
        )

    async def capas_shape_de_estaciones_climatolgicas_(self, tipoestacion):
        """Capas SHAPE de estaciones climatológicas de AEMET.

        Capas SHAPE de las distintas estaciones climatológicas de AEMET:
        automáticas, completas, pluviométricas y termométricas.

        :param str tipoestacion: Tipo de Estación
                                    automaticas    -> Estaciones Automáticas
                                    completas      -> Estaciones Completas
                                    pluviometricas -> Estaciones Pluviométricas
                                    termometricas  -> Estaciones Termométricas
        """
        return self._aemetClient.request(
            "/api/productos/climatologicos/capasshape/" + tipoestacion
        )

    async def resumen_mensual_climatolgico_nacional__documento_(self, anio, mes):
        """Resumen mensual climatológico nacional (documento).

        Resumen climatológico nacional, para el año y mes pasado por
        parámetro, sobre el estado del clima y la evolución de las
        principales variables climáticas, en especial temperatura y
        precipitación, a nivel mensual, estacional y anual.

        :param str anio: Año (AAAA)
        :param str mes: Mes (mm)
        """
        return self._aemetClient.request(
            "/api/productos/climatologicos/resumenclimatologico/nacional/"
            + anio
            + "/"
            + mes
        )


class RedRadaresApi(object):
    """Imagen nacional radares."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient

    async def imagen_composicin_nacional_radares__tiempo_actual_estndar_(self):
        """Imagen composición nacional radares. Tiempo actual estándar.

        Imagen composición nacional radares. Tiempo actual estándar.
        Periodicidad: 30 minutos.
        """
        return self._aemetClient.request("/api/red/radar/nacional")

    async def radar_regional(self, radar):
        """Imagen gráfica radar regional. Tiempo actual estándar.

        Imagen del radar regional de la región pasada por parámetro.
        Tiempo actual estándar. Periodicidad: 10 minutos.

        :param str radar: Código Radar
                                am -> Almería
                                sa -> Asturias
                                pm -> Illes Balears
                                ba -> Barcelona
                                cc -> Cáceres
                                co -> A Coruña
                                ma -> Madrid
                                ml -> Málaga
                                mu -> Murcia
                                vd -> Palencia
                                ca -> Las Palmas
                                se -> Sevilla
                                va -> Valencia
                                ss -> Vizcaya
                                za -> Zaragoza
        """
        return self._aemetClient.request("/api/red/radar/regional/" + radar)


class RedRayosApi(object):
    """Mapa con los rayos."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient

    async def mapa_con_los_rayos_registrados_en_periodo_standard__ltimo_elaborado_(
        self,
    ):
        """Mapa con los rayos registrados en periodo standard. Último elaborado.

        Imagen de las descargas caídas en el territorio nacional durante un
        período de 12 horas.
        """
        return self._aemetClient.request("/api/red/rayos/mapa")


class RedesEspecialesApi(object):
    """Redes especiales."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient

    async def contenido_total_de_ozono__tiempo_actual_(self):
        """Contenido total de ozono. Tiempo actual.

        Dato medio diario de contenido total de ozono.
        Cada 24 h (actualmente, en fines de semana, festivos y vacaciones
        no se genera por la falta de personal en
        el Centro Radiométrico Nacional).
        """
        return self._aemetClient.request("/api/red/especial/ozono")

    async def datos_de_contaminacin_de_fondo__tiempo_actual_(self, nombre_estacion):
        """Datos de contaminación de fondo. Tiempo actual.

        Ficheros diarios con datos diezminutales de la estación de la red
        de contaminación de fondo EMEP/VAG/CAMP pasada por parámetro,
        de temperatura, presión, humedad, viento (dirección y velocidad),
        radiación global, precipitación y 4 componentes
        químicos: O3,SO2,NO,NO2 y PM10. Los datos se encuentran en
        formato FINN (propio del Ministerio de Medio Ambiente).
        Periodicidad: cada hora.

        :param str nombre_estacion: Código Estación de la Red EMEP
                                        11 -> Barcarrota (Badajoz)
                                        10 -> Cabo de Creus (Girona)
                                        09 -> Campisábalos (Guadalajara)
                                        17 -> Doñana (Huelva)
                                        14 -> Els Torms (Lleida)
                                        06 -> Mahón (Illes Balears)
                                        08 -> Niembro-Llanes (Asturias)
                                        05 -> Noia (A Coruña)
                                        16 -> O Saviñao (Lugo)
                                        13 -> Peñausende (Zamora)
                                        01 -> San Pablo de los Montes (Toledo)
                                        07 -> Víznar (Granada)
                                        12 -> Zarra (Valencia)
        """
        return self._aemetClient.request(
            "/api/red/especial/contaminacionfondo/estacion/" + nombre_estacion
        )

    async def datos_de_radiacin_global_directa_o_difusa__tiempo_actual_(self):
        """Datos de radiación global, directa o difusa. Tiempo actual.

        Datos horarios (HORA SOLAR VERDADERA) acumulados de radiación global,
        directa, difusa e infrarroja, y datos
        semihorarios (HORA SOLAR VERDADERA) acumulados de radiación
        ultravioleta eritemática.Datos diarios acumulados de radiación global,
        directa, difusa, ultravioleta eritemática e infrarroja.
        Periodicidad: Cada 24h (actualmente en fines de semana, festivos y
        vacaciones, no se genera por la ausencia de personal en
        el Centro Radiométrico Nacional).
        """
        return self._aemetClient.request("/api/red/especial/radiacion")

    async def perfiles_verticales_de_ozono__tiempo_actual_(self, estacion):
        """Perfiles verticales de ozono. Tiempo actual.

        Perfil Vertical de Ozono de la estación pasada por parámetro.
        Periodicidad: cada 7 días.

        :param str estacion: Código Estación
                                canarias  -> Izaña
                                peninsula -> Madrid
        """
        return self._aemetClient.request(
            "/api/red/especial/perfilozono/estacion/" + estacion
        )


class ValoresClimatologicosApi(object):
    """Valores climatológicos."""

    def __init__(self):
        """Initialize."""
        self._aemetClient = aemetClient

    async def climatologas_diarias_(self, fechaIniStr, fechaFinStr, idema):
        """Climatologías diarias.

        Valores climatológicos para el rango de fechas y la estación
        seleccionada.
        Periodicidad: 1 vez al día.

        :param str fechaIniStr: Fecha Inicial (AAAA-MM-DDTHH:MM:SSUTC)
        :param str fechaFinStr: Fecha Final (AAAA-MM-DDTHH:MM:SSUTC)
        :param str idema: Indicativo climatológico de la EMA.
                                Puede introducir varios indicativos separados por comas (,)
        """
        return self._aemetClient.request(
            "/api/valores/climatologicos/diarios/datos/fechaini/"
            + fechaIniStr
            + "/fechafin/"
            + fechaFinStr
            + "/estacion/"
            + idema
        )

    async def climatologas_diarias_1(self, fechaIniStr, fechaFinStr):
        """Climatologías diarias.

        Valores climatológicos de todas las estaciones para el rango de
        fechas seleccionado.
        Periodicidad: 1 vez al día.

        :param str fechaIniStr: Fecha Inicial (AAAA-MM-DDTHH:MM:SSUTC)
        :param str fechafin: Fecha Final (AAAA-MM-DDTHH:MM:SSUTC)
        """
        return self._aemetClient.request(
            "/api/valores/climatologicos/diarios/datos/fechaini/"
            + fechaIniStr
            + "/fechafin/"
            + fechaFinStr
            + "/todasestaciones"
        )

    async def climatologas_mensuales_anuales_(self, anioIniStr, anioFinStr, idema):
        """Climatologías mensuales anuales.

        Valores medios mensuales y anuales de los datos climatológicos para
        la estación y el periodo de años pasados por parámetro.
        Periodicidad: 1 vez al día.

        :param str anioIniStr: Año Inicial (AAAA)
        :param str anioFinStr: Año Final (AAAA)
        :param str idema: Indicativo climatológico de la EMA
        """
        return self._aemetClient.request(
            "/api/valores/climatologicos/mensualesanuales/datos/anioini/"
            + anioIniStr
            + "/aniofin/"
            + anioFinStr
            + "/estacion/"
            + idema
        )

    async def climatologas_normales__19812010_(self, idema):
        """Climatologías normales (1981-2010).

        Valores climatológicos normales (periodo 1981-2010) para la estación
        pasada por parámetro.
        Periodicidad: 1 vez al día.

        :param str idema: Indicativo climatológico de la EMA
        """
        return self._aemetClient.request(
            "/api/valores/climatologicos/normales/estacion/" + idema
        )

    async def estaciones_por_indicativo_(self, estaciones):
        """Estaciones por indicativo.

        Características de la estación climatológica pasada por parámetro.

        :param str estaciones: Listado de indicativos climatológicos (id1,id2,id3,...,idn)
        """
        return self._aemetClient.request(
            "/api/valores/climatologicos/inventarioestaciones/estaciones/" + estaciones
        )

    async def inventario_de_estaciones__valores_climatolgicos_(self):
        """Inventario de estaciones (valores climatológicos).

        Inventario con las características de todas las estaciones
        climatológicas.
        Periodicidad: 1 vez al día.
        """
        return self._aemetClient.request(
            "/api/valores/climatologicos/inventarioestaciones/todasestaciones"
        )

    async def valores_extremos_(self, parametro, idema):
        """Valores extremos.

        Valores extremos para la estación y la variable (precipitación,
        temperatura y viento) pasadas por parámetro.
        Periodicidad: 1 vez al día.

        :param str parametro: Código Parámetro Meteorológico
                                    P -> Precipitación
                                    T -> Temperatura
                                    V -> Viento
        :param str idema: Indicativo climatológico de la EMA
        """
        return self._aemetClient.request(
            "/api/valores/climatologicos/valoresextremos/parametro/"
            + parametro
            + "/estacion/"
            + idema
        )
