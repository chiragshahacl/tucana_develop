export enum RESPONSE_STATUS {
  METRIC = 'metric',
  WAVEFORM = 'waveform',
  SENSOR_DATA = 'sensor_data',
  DEVICE_REFRESH = 'device_refresh',
  BEDS_REFRESH = 'beds_refresh',
  FULL_REFRESH = 'full_refresh',
  BED_GROUP_REFRESH = 'bed_group_refresh',
  RECONNECTION_NEEDED = 'reconnection_needed',
  ALERT = 'alert',
  REFRESH_ALERT_HISTORY = 'refresh_alert_history',
  NEW_RANGE = 'new_range',
  PM_STATUS_REPORT = 'pm_status_report',
  PATIENT_REFRESH = 'patient_refresh',
  BEDSIDE_AUDIO_ALERT_STATUS = 'bedside_audio_alert_status',
  PATIENT_SESSION_CLOSED = 'patient_session_closed',
  PATIENT_ENCOUNTER_CANCELLED = 'patient_encounter_cancelled',
  SENSOR_DISCONNECTED = 'sensor_disconnected',
  BATTERY_STATUS = 'battery_status',
}