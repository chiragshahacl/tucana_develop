import React from 'react';

const AudioOff = ({ color = '#34B2EA' }: { color?: string }) => {
  return (
    <svg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'>
      <path
        fillRule='evenodd'
        clipRule='evenodd'
        d='M12.5689 2.91255C15.5204 3.24686 17.0271 5.38428 17.6919 6.73996L20.1333 4.46096L22.5747 2.18195C22.8956 1.88245 23.3851 1.91492 23.6681 2.25449C23.9511 2.59405 23.9204 3.11212 23.5996 3.41163L18.3016 8.35713C18.8121 9.92268 19.9711 13.508 20.8525 16.2376C21.2121 17.3512 20.6755 18.497 19.7443 18.9393L23.7297 22.5579C24.0544 22.8528 24.0918 23.3703 23.8133 23.714C23.5347 24.0576 23.0457 24.0972 22.721 23.8024L17.5742 19.1293H13.5619C13.9084 19.5495 14.1182 20.0991 14.1182 20.7006C14.1182 22.0212 13.1067 23.0918 11.8589 23.0918C10.611 23.0918 9.59948 22.0212 9.59948 20.7006C9.59948 20.0991 9.80933 19.5495 10.1558 19.1293H6.76172L1.78046 23.7791C1.45961 24.0786 0.970093 24.0462 0.687096 23.7066C0.4041 23.367 0.434786 22.849 0.755636 22.5495L4.43683 19.1132C3.1594 18.9498 2.30568 17.5706 2.73609 16.2376C3.67876 13.3182 4.93901 9.41993 5.38378 8.06081L0.27026 3.4179C-0.0544408 3.12309 -0.0918389 2.60551 0.18673 2.26187C0.465299 1.91823 0.954347 1.87865 1.27905 2.17347L6.02735 6.48477C6.74989 5.13119 8.24754 3.22654 11.0197 2.91255V0H12.5689V2.91255ZM11.7943 4.50767C14.7574 4.52288 16.0467 6.79177 16.4856 7.866L12.079 11.9794L7.22993 7.57667C7.76681 6.43162 9.07647 4.52162 11.7943 4.50767ZM4.20213 16.7678C5.03171 14.1986 6.10087 10.8912 6.64828 9.20893L10.9058 13.0746L6.17609 17.4896H4.69106C4.33591 17.4896 4.08803 17.1212 4.20213 16.7678ZM8.51823 17.4896L12.0931 14.1526L15.7683 17.4896H8.51823ZM18.8975 17.4896H18.1477L13.2663 13.0575L17.0448 9.5303C17.6157 11.2872 18.6069 14.3535 19.3865 16.7678C19.5006 17.1212 19.2527 17.4896 18.8975 17.4896Z'
        fill={color}
      />
    </svg>
  );
};

export default AudioOff;