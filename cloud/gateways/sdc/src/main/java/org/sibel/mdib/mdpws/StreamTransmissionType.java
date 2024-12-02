//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.3.0.1
// See <a href="https://javaee.github.io/jaxb-v2/">https://javaee.github.io/jaxb-v2/</a>
// Any modifications to this file will be lost upon recompilation of the source schema.
// Generated on: 2024.05.09 at 01:02:24 PM UTC
//

package org.sibel.mdib.mdpws;

import java.util.HashMap;
import java.util.Map;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAnyAttribute;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlSchemaType;
import javax.xml.bind.annotation.XmlType;
import javax.xml.datatype.Duration;
import javax.xml.namespace.QName;

/**
 * Definition of the mechanisms that are utilized to transmit a stream.
 *
 * <p>Java class for StreamTransmissionType complex type.
 *
 * <p>The following schema fragment specifies the expected content contained within this class.
 *
 * <pre>
 * &lt;complexType name="StreamTransmissionType"&gt;
 *   &lt;complexContent&gt;
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType"&gt;
 *       &lt;sequence&gt;
 *         &lt;element name="StreamAddress" type="{http://www.w3.org/2001/XMLSchema}anyURI" minOccurs="0"/&gt;
 *         &lt;element name="StreamPeriod" type="{http://www.w3.org/2001/XMLSchema}duration" minOccurs="0"/&gt;
 *       &lt;/sequence&gt;
 *       &lt;attribute name="Type" type="{http://www.w3.org/2001/XMLSchema}anyURI" /&gt;
 *       &lt;anyAttribute processContents='skip' namespace='##other'/&gt;
 *     &lt;/restriction&gt;
 *   &lt;/complexContent&gt;
 * &lt;/complexType&gt;
 * </pre>
 *
 *
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(
        name = "StreamTransmissionType",
        propOrder = {"streamAddress", "streamPeriod"})
public class StreamTransmissionType {

    @XmlElement(name = "StreamAddress")
    @XmlSchemaType(name = "anyURI")
    protected String streamAddress;

    @XmlElement(name = "StreamPeriod")
    protected Duration streamPeriod;

    @XmlAttribute(name = "Type")
    @XmlSchemaType(name = "anyURI")
    protected String type;

    @XmlAnyAttribute
    private Map<QName, String> otherAttributes = new HashMap<QName, String>();

    /**
     * Gets the value of the streamAddress property.
     *
     * @return
     *     possible object is
     *     {@link String }
     *
     */
    public String getStreamAddress() {
        return streamAddress;
    }

    /**
     * Sets the value of the streamAddress property.
     *
     * @param value
     *     allowed object is
     *     {@link String }
     *
     */
    public void setStreamAddress(String value) {
        this.streamAddress = value;
    }

    /**
     * Gets the value of the streamPeriod property.
     *
     * @return
     *     possible object is
     *     {@link Duration }
     *
     */
    public Duration getStreamPeriod() {
        return streamPeriod;
    }

    /**
     * Sets the value of the streamPeriod property.
     *
     * @param value
     *     allowed object is
     *     {@link Duration }
     *
     */
    public void setStreamPeriod(Duration value) {
        this.streamPeriod = value;
    }

    /**
     * Gets the value of the type property.
     *
     * @return
     *     possible object is
     *     {@link String }
     *
     */
    public String getType() {
        return type;
    }

    /**
     * Sets the value of the type property.
     *
     * @param value
     *     allowed object is
     *     {@link String }
     *
     */
    public void setType(String value) {
        this.type = value;
    }

    /**
     * Gets a map that contains attributes that aren't bound to any typed property on this class.
     *
     * <p>
     * the map is keyed by the name of the attribute and
     * the value is the string value of the attribute.
     *
     * the map returned by this method is live, and you can add new attribute
     * by updating the map directly. Because of this design, there's no setter.
     *
     *
     * @return
     *     always non-null
     */
    public Map<QName, String> getOtherAttributes() {
        return otherAttributes;
    }
}
