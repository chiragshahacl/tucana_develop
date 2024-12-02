import { SENSOR_TYPES } from '@/types/sensor';
import { getAlertColor } from '@/utils/alertUtils';
import { ALERT_PRIORITY } from '@/utils/metricCodes';

type Props = {
  alertPriority?: ALERT_PRIORITY;
};

const LimbSensorIcon = ({ alertPriority }: Props) => {
  const color = alertPriority ? getAlertColor(alertPriority) : 'white';
  return (
    <svg
      data-testid={`${SENSOR_TYPES.LIMB}-sensor-icon`}
      height='40'
      viewBox='0 0 40 40'
      fill='none'
      xmlns='http://www.w3.org/2000/svg'
    >
      <g clipPath='url(#clip0_1614_15951)'>
        <path
          fillRule='evenodd'
          clipRule='evenodd'
          d='M12.5 26.8357C12.5 27.5601 12.736 28.0587 13.1024 28.45C13.4181 28.7871 13.8272 29.0386 14.2186 29.2792C14.271 29.3114 14.323 29.3434 14.3745 29.3754C14.8184 29.6512 15.2377 29.9353 15.5512 30.3557C15.8632 30.7741 16.0804 31.3417 16.0804 32.1921L16.0804 37.9673C16.0804 39.0936 16.5587 40 17.9952 40L22.6298 39.9997C24.0663 39.9997 24.5446 39.0933 24.5446 37.967V32.1918C24.5446 31.3414 24.7618 30.7738 25.0738 30.3554C25.3873 29.935 25.8066 29.6508 26.2505 29.3751C26.302 29.3431 26.354 29.3111 26.4064 29.2789C26.7978 29.0383 27.2069 28.7868 27.5226 28.4497C27.889 28.0584 28.125 27.5598 28.125 26.8353L28.0496 12.9281C28.0496 12.1906 27.7433 11.6939 27.274 11.3192C26.8626 10.9907 26.3289 10.7606 25.8191 10.5409L25.8163 10.5397C25.7627 10.5165 25.7093 10.4935 25.6563 10.4705L25.6198 10.4546C25.0387 10.2022 24.7116 10.0601 24.4807 9.59993C24.2242 9.08891 24.2356 8.82737 24.2554 8.37477C24.2615 8.23447 24.2685 8.0758 24.2685 7.88565V3.24322C24.2685 1.45204 24.17 0 22.3941 0L18.2309 0.000314111C16.455 0.000314111 16.3565 1.45235 16.3565 3.24353L16.3565 7.88597C16.3565 8.07612 16.3635 8.23478 16.3696 8.37509C16.3894 8.82768 16.4008 9.08922 16.1443 9.60024C15.9134 10.0604 15.5863 10.2025 15.0052 10.4549L14.9687 10.4708C14.9157 10.4938 14.8623 10.5168 14.8087 10.54L14.8059 10.5412C14.2961 10.761 13.7624 10.9911 13.351 11.3195C12.8817 11.6942 12.5754 12.1909 12.5754 12.9284L12.5 26.8357ZM16.6017 12.6859C15.0862 12.6859 13.8577 13.914 13.8577 15.4288V18.1716C13.8577 19.6864 15.0862 20.9145 16.6017 20.9145H24.1476C25.6631 20.9145 26.8916 19.6864 26.8916 18.1716V15.4288C26.8916 13.914 25.6631 12.6859 24.1476 12.6859H16.6017ZM18.2309 3.78407C18.2309 2.88848 18.9507 2.16246 19.8387 2.16246H20.9106C21.7985 2.16246 22.5184 2.88848 22.5184 3.78407V4.86514C22.5184 5.76073 21.7985 6.48675 20.9106 6.48675H19.8387C18.9507 6.48675 18.2309 5.76073 18.2309 4.86514V3.78407Z'
          fill={color}
        />
        <path
          d='M25.2909 13.9431H24.6049C24.9838 13.9431 25.2909 14.5827 25.2909 15.3717V18.2288C25.2909 19.0177 24.9838 19.6573 24.6049 19.6573H25.2909C25.6698 19.6573 25.9769 19.0177 25.9769 18.2288V15.3717C25.9769 14.5827 25.6698 13.9431 25.2909 13.9431Z'
          fill={color}
        />
        <path
          d='M21.1749 2.97173H21.6323C21.8848 2.97173 22.0896 3.25315 22.0896 3.6003V4.85743C22.0896 5.20458 21.8848 5.48599 21.6323 5.48599H21.1749C21.4275 5.48599 21.6323 5.20458 21.6323 4.85743V3.6003C21.6323 3.25315 21.4275 2.97173 21.1749 2.97173Z'
          fill={color}
        />
        <path
          d='M21.4269 16.4587C21.1362 16.1709 20.7861 16.027 20.3746 16.027C19.9979 16.027 19.6232 16.1932 19.2486 16.5236V15.0319C19.2486 14.9833 19.2301 14.9407 19.1974 14.9063C19.1626 14.8738 19.1216 14.8576 19.0725 14.8576H19.0643C19.0152 14.8576 18.9742 14.8738 18.9394 14.9063C18.9046 14.9407 18.8882 14.9833 18.8882 15.0319V17.5086C18.8903 17.9119 19.0356 18.2564 19.3264 18.5442C19.615 18.83 19.9651 18.9719 20.3746 18.9719C20.7861 18.9719 21.1362 18.828 21.4269 18.5422C21.7176 18.2544 21.8609 17.9078 21.8609 17.5005C21.8609 17.0931 21.7155 16.7465 21.4269 16.4587ZM21.1689 18.2949C20.9519 18.5138 20.6858 18.6233 20.3725 18.6233C20.0613 18.6233 19.7952 18.5138 19.5741 18.2949C19.355 18.0761 19.2465 17.8146 19.2465 17.5086C19.2465 17.2005 19.355 16.937 19.5741 16.7181C19.7952 16.4993 20.0613 16.3898 20.3725 16.3898C20.6858 16.3898 20.9499 16.4993 21.1689 16.7181C21.39 16.937 21.5006 17.2005 21.5006 17.5086C21.5006 17.8146 21.39 18.0781 21.1689 18.2949Z'
          fill={color}
        />
        <path
          d='M21.3457 17.1469C21.2904 16.9969 21.1472 16.8895 20.9773 16.8895C20.7605 16.8895 20.5845 17.0638 20.5845 17.2787C20.5845 17.4408 20.6847 17.5786 20.8259 17.6374C20.83 17.6435 20.8362 17.6475 20.8403 17.6536C20.1589 17.6536 20.2305 18.213 20.1486 18.294C20.0688 18.3751 19.9952 18.3326 19.9481 18.3792C19.9277 18.3994 19.9174 18.44 19.9256 18.4623C20.0484 18.5109 20.1793 18.5332 20.3205 18.5332C20.6193 18.5332 20.8709 18.4298 21.0776 18.2211C21.2884 18.0123 21.3927 17.763 21.3927 17.4712C21.3927 17.3658 21.3784 17.2665 21.3518 17.1733'
          fill={color}
        />
      </g>
      <defs>
        <clipPath id='clip0_1614_15951'>
          <rect width='40' height='40' fill={color} />
        </clipPath>
      </defs>
    </svg>
  );
};

export default LimbSensorIcon;
