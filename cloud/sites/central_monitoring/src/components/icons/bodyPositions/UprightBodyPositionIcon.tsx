import { useTheme } from '@mui/material/styles';

const UprightBodyPositionIcon = ({ darkIcon = false }: { darkIcon?: boolean }) => {
  const theme = useTheme();

  return (
    <svg
      data-testid='upright-position'
      width='68'
      height='30'
      viewBox='0 0 68 30'
      fill='none'
      xmlns='http://www.w3.org/2000/svg'
    >
      <path
        d='M18.9287 0.803833C16.8444 1.33847 15.5885 3.4615 16.1231 5.54565C16.6578 7.62977 18.7808 8.88582 20.8649 8.35109C22.9491 7.81645 24.2051 5.69341 23.6705 3.60927C23.1357 1.52515 21.0128 0.269099 18.9287 0.803833Z'
        fill={darkIcon ? theme.palette.common.black : theme.palette.divider}
      />
      <path
        d='M17.8227 11.6208C17.8259 11.5274 17.8292 11.4691 17.8309 11.4458C17.8796 10.7299 18.4909 10.0768 19.2234 9.95902C19.2429 9.95585 19.2619 9.95335 19.2818 9.95089C20.0286 9.86081 20.5976 10.3824 20.5501 11.1319L20.5483 11.1851C20.5414 11.9314 20.6673 15.0466 22.993 18.5144C23.7622 19.6618 24.7717 20.8477 26.0976 21.9992C26.6062 22.44 26.5701 23.2825 26.0164 23.8768C25.7555 24.1573 25.4161 24.3431 25.0602 24.4005C24.6871 24.4605 24.3426 24.3733 24.0901 24.1546C20.4114 20.9684 18.8856 17.4833 18.2559 14.9872C17.8046 13.1976 17.8128 11.9153 17.8227 11.6208Z'
        fill={darkIcon ? theme.palette.common.black : theme.palette.divider}
      />
      <path
        d='M32.091 22.6058C31.3772 22.6055 30.4849 22.4278 29.8194 22.2742C29.8021 22.0604 29.7858 21.8504 29.7704 21.6528C29.7293 21.1245 29.695 20.6839 29.6678 20.4953C29.314 18.0332 27.4245 13.56 25.1956 11.1327C24.1888 10.0362 22.6804 9.3074 20.9656 9.09873C20.3806 9.02754 19.7847 9.13543 19.2491 9.39611C19.8198 9.34602 20.3723 9.51506 20.7824 9.88968C21.2079 10.2783 21.4213 10.8348 21.3868 11.428L21.386 11.4535C21.3859 11.4599 21.3858 11.4663 21.3857 11.4727C21.3828 12.1486 21.5128 15.0073 23.6882 18.2044C24.4167 19.2754 25.3765 20.3885 26.6455 21.4747C27.6252 22.3117 27.3958 23.7033 26.6287 24.5149C26.249 24.917 25.7439 25.1961 25.1919 25.2839C24.6099 25.3762 24.0047 25.2482 23.5382 24.85C23.0007 24.3912 22.5071 23.926 22.0537 23.4581C22.4527 25.8033 23.2914 29.0004 25.526 29.0004C26.13 29.0016 26.708 28.9895 27.1928 28.9508C27.7701 28.9047 28.1816 28.8414 28.5926 28.7781C29.3772 28.6574 30.16 28.537 32.091 28.537C32.9094 28.537 34.1928 28.4783 35.7443 28.4073C39.4991 28.2355 44.8243 27.9918 48.9316 28.3346C49.104 28.3692 49.2755 28.3859 49.4447 28.3859C50.6329 28.3859 51.697 27.5638 51.9438 26.3714C52.2257 25.0091 51.334 23.6802 49.9519 23.4021C41.7276 22.7719 34.5862 22.6067 32.091 22.6058Z'
        fill={darkIcon ? theme.palette.common.black : theme.palette.divider}
      />
    </svg>
  );
};

export default UprightBodyPositionIcon;
